%global _legacy_common_support 1
Name:           libtpcimgio
Version:        1.5.10
Release:        36%{?dist}
Summary:        Turku PET Centre for image file input and output procedures

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.turkupetcentre.net/software/libdoc/%{name}/index.html
Source0:        http://www.turkupetcentre.net/software/libsrc/%{name}_1_5_10_src.zip
Patch0:         %{name}-add-header.patch
Patch1:         %{name}-shared.patch
Patch2:         %{name}-strings-header.patch
BuildRequires:  gcc
BuildRequires:  libtpcmisc-devel
BuildRequires:  doxygen dos2unix
BuildRequires:  graphviz
BuildRequires: make


%description
The libtpcimgio library is a collection of commonly used C files 
in Turku PET Centre for image file input and output procedures. 
Libtpcimgio library supports Analyze 7.5, Ecat 6.x, Ecat 7.x and 
partly interfile formats.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static libraries for %{name}

%description    static
This package contains static libraries for %{name}.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1 -b .shared
%patch -P2 -p1 -b .strings-header
sed -i "/^CFLAGS/d" Makefile

# Fix encodings and line endings.
dos2unix -k History Readme TODO
iconv -f ISO_8859-1 -t utf8 -o History.new History && mv -f History.new History


%build
# c99 standard since they use declarations in the for loops
# includedirs since it doesn't find them on their own
# the _XOPEN_SOURCE for timezone declaration
# undefine STRICT_ANSI since c99 sets it, and it conflicts with the strings.h declaration
# PIC for shared objects

export CFLAGS="%{optflags} -std=c99 -Iinclude/ -I%{_includedir}/libtpcmisc/ -D_XOPEN_SOURCE -U__STRICT_ANSI__ -fPIC -DPIC"
export CXXFLAGS="%{optflags} -fPIC -DPIC"
make %{?_smp_mflags}

# Build doxygen documentation
mkdir doc
( cat Doxyfile ; echo "OUTPUT_DIRECTORY=./doc" ) | doxygen -


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}

install -p -m 0755 %{name} -t $RPM_BUILD_ROOT%{_bindir}/
install -p -m 0644 %{name}.a -t $RPM_BUILD_ROOT%{_libdir}/
install -p -m 0755 %{name}.so.0.0.0 -t $RPM_BUILD_ROOT%{_libdir}/
install -p -m 0644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/

pushd $RPM_BUILD_ROOT%{_libdir}/
ln -s %{name}.so.0.0.0 %{name}.so.0
ln -s %{name}.so.0.0.0 %{name}.so
popd

%ldconfig_scriptlets

%files
%doc History Readme TODO
%{_bindir}/%{name}
%{_libdir}/%{name}.so.*

%files devel
%doc doc/%{name}/*
%{_libdir}/%{name}.so
%{_includedir}/*

%files static
%{_libdir}/%{name}.a

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.10-35
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Peter Fordham <peter.fordham@gmail.com> - 1.5.10-29
- Add string.h include for strcasecmp for C99 compatibility.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Jeff Law <law@redhat.com> - 1.5.10-24
- Enable _legacy_common_support

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.10-17
- Add gcc to BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.10-5
- spec bump for gcc 4.7 rebuild

* Mon Aug 08 2011 Tom Callaway <spot@fedoraproject.org> - 1.5.10-4
- compile with -fPIC so that xmedcon can use it in shared libs later
- build shared libs, put static libs in separate subpackage

* Mon Aug 01 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.10-3
- Add graphviz to BR

* Sun Jul 31 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.10-2
- Changes that Richard made:
- Add more documentation
- Fix line endings and encoding
- Add architecture specific requires
- https://bugzilla.redhat.com/show_bug.cgi?id=714327#c1

* Fri Jun 17 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.10-1
- initial rpm build
