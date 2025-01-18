Name:           fstrcmp
Version:        0.7.D001
Release:        25%{?dist}
Summary:        Fuzzy string compare library

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://fstrcmp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  man-db
BuildRequires: make

%description
The fstrcmp package provides a library which may be used to make fuzzy
comparisons of strings and byte arrays. It also provides simple commands for use
in shell scripts.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%check
# make t0001a ... t0010a
make $(seq -f "t%04ga" 1 10)


%install
%make_install
find $RPM_BUILD_ROOT \( -name "*.la" -o -name "*.a" \) -delete

# Fix permissions
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.*

# Remove useless compilation instructions
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/building.pdf
# Remove API documentation in main subpackage
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/reference.pdf
# Remove duplicate README in PDF
rm $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/readme.pdf


%ldconfig_scriptlets


%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}*.1.*


%files devel
%doc etc/reference.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.D001-24
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.D001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 12 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.D001-4
- Drop duplicate PDF documentation

* Wed Aug 12 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.D001-3
- Unmark license man page as %%license

* Thu Jul 30 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.D001-2
- Fix duplicates in %%files
- Mark license man page as %%license
- Add unit tests in %%check

* Tue Jul 28 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.7.D001-1
- Initial RPM release
