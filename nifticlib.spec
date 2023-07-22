Name:           nifticlib
Version:        2.0.0
Release:        30%{?dist}
Summary:        A set of i/o libraries for reading and writing files in the nifti-1 data format

License:        Public Domain
URL:            http://niftilib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/niftilib/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  zlib-devel doxygen cmake gcc gcc-c++

%description
Nifticlib is a set of C i/o libraries for reading and writing files in
the nifti-1 data format. nifti-1 is a binary file format for storing
medical image data, e.g. magnetic resonance image (MRI) and functional
MRI (fMRI) brain images.

%package devel
Summary: Libraries and header files for nifticlib development
Requires: %{name} = %{version}-%{release}

%description devel
The nifticlib-devel package contains the header files and libraries
necessary for developing programs that make use of the nifticlib library.

%package docs
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description docs
The package contains documentation and example files for %{name}.

%prep
%setup -q
sed -i "s|csh|$SHELL|" Makefile

%build
# make the doc
make doc %{?_smp_mflags}

# cmake replaces the original makefile so I call it after generating my docs
%cmake -DBUILD_SHARED_LIBS=ON .
%cmake_build

%install
rm -rf %{buildroot}
%cmake_install

## hack to get this to work for x86_64
%if "%{_lib}" == "lib64" 
    install -p -d %{buildroot}/%{_libdir}/
    mv -v %{buildroot}/usr/lib/* %{buildroot}/%{_libdir}/
    rm -rvf %{buildroot}/usr/lib/
%endif

# remove extra files
rm -fv docs/html/installdox
rm -fv docs/html/Doxy*

%files
%doc README Updates.txt
%license LICENSE
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/nifti/

%files docs
%doc examples
%doc docs

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 30 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-24
- Update to use cmake macros to fix build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-17
- Add gcc g++ to BR
- Use license macro
- Use buildroot instead of RPM_BUILD_ROOT

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.0.0-8
- Fix docs
- https://bugzilla.redhat.com/show_bug.cgi?id=1001274

* Fri Oct 11 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.0.0-7
- https://bugzilla.redhat.com/show_bug.cgi?id=1001238

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-3
- spec bump for gcc 4.7 rebuild

* Tue Jul 26 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-2
- Correct source URL

* Fri Jun 17 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.0-1
- initial rpm build
- based on the spec built by Andy Loening <loening at alum dot mit dot edu> in the source tar
