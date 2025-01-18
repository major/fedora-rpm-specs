# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global upstream_name FoX

Name:		FoXlibf
Version:	4.1.2
Release:	26%{?dist}
Summary:	A Fortran XML Library
# Automatically converted from old format: zlib and BSD - review is highly recommended.
License:	Zlib AND LicenseRef-Callaway-BSD
URL:		http://www1.gly.bris.ac.uk/~walker/FoX/
Source0:	http://www1.gly.bris.ac.uk/~walker/FoX/source/%{upstream_name}-%{version}.tar.gz
Patch0:		FoX-4.1.2-DESTDIR.patch
Patch1:		FoX-4.1.2-system-paths.patch
Patch2:		FoX-4.1.2-sharedlibs.patch
Patch3:		FoX-4.1.2-dompp.patch
BuildRequires:	gcc-gfortran
BuildRequires: make

%description
FoX is an XML library written in Fortran 95. It allows software developers to
read, write and modify XML documents from Fortran applications without the 
complications of dealing with multiple language development.

%package devel
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Development files for FoX

%description devel
Development files for FoX.

%package static
Requires:	%{name}%{?_isa} = %{version}-%{release}
Summary:	Static libraries for FoX

%description static
Static libraries for FoX.

%prep
%setup -qn %{upstream_name}-%{version}
%patch -P0 -p1 -b .DESTDIR
%patch -P1 -p1 -b .system
%patch -P2 -p1 -b .shared

# We need a variant "pretty-print" version of the dom library for exciting
cp -a dom dompp
sed -i "s/ 27293398$/ ibset(27293398,22)/" dompp/m_dom_dom.F90 
sed -i "s|libFoX_dom|libFoX_dompp|g" dompp/makefile

%patch -P3 -p1 -b .dompp

%build
export FCFLAGS="%{optflags} %{?_fmoddir: -I%_fmoddir} -fPIC"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
pushd %{buildroot}%{_libdir}
for i in libFoX_common libFoX_dom libFoX_dompp libFoX_fsys libFoX_sax libFoX_utils libFoX_wcml libFoX_wkml libFoX_wxml; do
	ln -s $i.so.0.0.0 $i.so.0
	ln -s $i.so.0.0.0 $i.so
done
chmod -x %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc README.FoX.txt
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/libFoX*.so.*

%files devel
%{_bindir}/FoX-config
%{_includedir}/FoX/
%{_libdir}/libFoX*.so

%files static
%{_libdir}/libFoX*.a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.2-25
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 4.1.2-19
- Change changelog email

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Oct 31 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 4.1.2-5
- Rebuilt for new gcc-gfortran on el7

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 4.1.2-2
- rebuild for gcc-gfortran-5.0.0

* Sat Nov 8 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 4.1.2-1
- renamed to FoXlibf

* Thu May 29 2014 Tom Callaway <spot@fedoraproject.org> - 4.1.2-1
- initial package
