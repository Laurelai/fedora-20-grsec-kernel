
Current version 3.17.2-200.grsec.fc20.x86_64


Instructions.

AS ROOT.
yum -y update

(restart if kernel was updated)

yum install rpmdevtools yum-utils gcc-plugin-devel pesign ncurses-devel qt3-devel libXi-devel gcc-c++

yum groupinstall "Development Tools"

yum-builddep kernel

AS REGULAR NON ROOT USER
rpmdev-setuptree
yumdownloader --source kernel
rpm -Uvh kernel-3.17.2-200.fc20.src.rpm

Aquire grsecurity-3.0-3.17.2-201411091054.patch from a trusted source!

Import spenders key! http://en.wikibooks.org/wiki/Grsecurity/Obtaining_grsecurity#Verifying_the_Downloads

TEST THE PATCH
gpg --verify grsecurity-3.0-3.17.2-201411091054.patch.sig

Open patch in your favorite text editor and remove the following block of code.

diff --git a/arch/x86/vdso/Makefile b/arch/x86/vdso/Makefile
index fd14be1..e3c79c0 100644
--- a/arch/x86/vdso/Makefile
+++ b/arch/x86/vdso/Makefile
@@ -181,7 +181,7 @@ quiet_cmd_vdso = VDSO    $@
           -Wl,-T,$(filter %.lds,$^) $(filter %.o,$^) && \
     sh $(srctree)/$(src)/checkundef.sh '$(NM)' '$@'

-VDSO_LDFLAGS = -fPIC -shared $(call cc-ldoption, -Wl$(comma)--hash-style=sysv)
+VDSO_LDFLAGS = -fPIC -shared -Wl,--no-undefined $(call cc-ldoption, -Wl$(comma)--hash-style=sysv)
 GCOV_PROFILE := n

 #
 
 
 
 Then do the same for this one.
 
 diff --git a/init/Kconfig b/init/Kconfig
index 4e5d96a..93cd8a1 100644
--- a/init/Kconfig
+++ b/init/Kconfig
@@ -1079,6 +1079,7 @@ endif # CGROUPS

 config CHECKPOINT_RESTORE
  bool "Checkpoint/restore support" if EXPERT
+ depends on !GRKERNSEC
  default n
  help
    Enables additional kernel features in a sake of checkpoint/restore.

And finally this.

diff --git a/localversion-grsec b/localversion-grsec
new file mode 100644
index 0000000..7cd6065
--- /dev/null
+++ b/localversion-grsec
@@ -0,0 +1 @@
+-grsec

Build witht he following command.

$ rpmbuild -bb --without debug --without debuginfo --without extra --without perf --without tools kernel.spec