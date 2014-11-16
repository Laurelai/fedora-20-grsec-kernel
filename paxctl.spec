Name:           paxctl
Version:        0.9
Release:        1%{?dist}
Summary:        PaX control program and regression tests

License:        GPL
URL:     http://pax.grsecurity.net       
Source0: %{name}-%{version}.tar.gz       
Source1: paxtest-0.9.11.tar.gz
# BuildRequires:  
# Requires:       

%description
New PaX control program when you use the PT_PAX_FLAGS marking
available in PaX patches after 2004.02.04. Also contains the
PaX regression test suite

%prep
%setup -q

tar zxf $RPM_SOURCE_DIR/paxtest-0.9.11.tar.gz
%build
rm -rf $RPM_BUILD_ROOT

make %{_smp_mflags}

cd paxtest-0.9.11
export RUNDIR=%{_libexecdir}/paxtest
make linux

%install
rm -rf $RPM_BUILD_ROOT

make %{_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/paxtest \
		$RPM_BUILD_ROOT/sbin

cd paxtest-0.9.11

# install tests
for i in anonmap execbss execdata execheap execstack mprotanon mprotbss mprotdata mprotheap mprotshbss mprotshdata mprotstack randamap randheap1 randheap2 randmain1 randmain2 randshlib randstack1 randstack2 rettofunc1 rettofunc1x rettofunc2 rettofunc2x shlibbss shlibdata writetext; do
	install -m 0755 $i $RPM_BUILD_ROOT/%{_libexecdir}/paxtest/
done

# isntall utils
for i in getamap getheap1 getheap2 getmain1 getmain2 getshlib getstack1 getstack2; do
    install -m 0755 $i $RPM_BUILD_ROOT/%{_libexecdir}/paxtest/
done

# install libs
for i in shlibtest.so shlibtest2.so; do
    install -m 0755 $i $RPM_BUILD_ROOT/%{_libexecdir}/paxtest/
done

# install wrapper script
install -m 0755 paxtest $RPM_BUILD_ROOT/sbin/
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/sbin/paxctl
/sbin/paxtest
%{_mandir}/man*/*
%dir
%{_libexecdir}/paxtest/


%changelog
* Sun Nov 16 2014 Laurelai Bailey
- 
