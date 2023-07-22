Name:             libcangjie
Summary:          Cangjie Input Method Library
Version:          1.3
Release:          20%{?dist}
License:          LGPLv3+
URL:              http://cangjians.github.io/projects/%{name}
Source0:          https://github.com/Cangjians/libcangjie/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:    gcc
BuildRequires:    sqlite-devel
BuildRequires: make

# Split out so it can be noarch
Requires:         %{name}-data = %{version}-%{release}

%description
Library implementing the Cangjie input method.


%package data
Summary:          Database for %{name}
BuildArch:        noarch

%description data
Database for %{name}.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{_isa} = %{version}-%{release}
Requires:         sqlite-devel

%description devel
Development files for %{name}.


%prep
%setup -q


%build
%configure

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f '{}' \;


%check
make check


%files
%doc AUTHORS COPYING README.md
%{_libdir}/%{name}.so.2*

%files data
%doc data/README.table.rst
%{_datadir}/%{name}

%files devel
%doc docs/*.md
%{_bindir}/libcangjie_*
%{_includedir}/cangjie
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/cangjie.pc


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.3-9
- Removed the ldconfig scriptlets.

* Sun Feb 18 2018 Mathieu Bridon <bochecha@daitauha.fr> - 1.3-8
- Added missing build requirement on gcc.
  https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/IJFYI5Q2BYZKIGDFS2WLOBDUSEGWHIKV/

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 28 2014 Mathieu Bridon <bochecha@daitauha.fr> - 1.3-1
- New upstream 1.3 release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 1.2-1
- New upstream 1.2 release.

* Sun Feb 02 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 1.1-1
- New upstream 1.1 release.

* Sun Dec 22 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 1.0-1
- New upstream 1.0 release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.0.1a-3
- Apply upstream patch to fix the classic frequency.

* Sat Apr 20 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.0.1a-2
- Split out the databases to a noarch subpackage, as suggested by Michael
  during the review.

* Sat Apr 20 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.0.1a-1
- Initial package for Fedora.
