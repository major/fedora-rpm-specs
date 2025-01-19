Name:           libjodycode
Version:        3.1.1
Release:        2%{?dist}
Summary:        General purpose utility functions

License:        MIT
URL:            https://codeberg.org/jbruchon/libjodycode/
Source0:        https://codeberg.org/jbruchon/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make


%description
libjodycode is a software code library containing code shared among
several of the programs written by Jody Bruchon such as imagepile,
jdupes, winregfs, and zeromerge. These shared pieces of code were
copied between each program as they were updated. As the number of
programs increased and keeping these pieces of code synced became more
annoying, the decision was made to combine all of them into a single
reusable shared library.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}


%build
%make_build HARDEN=1 PREFIX="%{_prefix}" LIB_DIR="%{_libdir}"


%install
%make_install HARDEN=1 PREFIX="%{_prefix}" LIB_DIR="%{_libdir}"

# Do not include the static library
rm -f %{buildroot}%{_libdir}/libjodycode.a

# man page is currently empty
rm -rf %{buildroot}%{_mandir}/man7


%files
%license LICENSE.txt
%doc CHANGES.txt README.md
%{_libdir}/libjodycode.so.*


%files devel
%{_includedir}/libjodycode.h
%{_libdir}/libjodycode.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Jonathan Wright <jonathan@almalinux.org> - 3.1.1-1
- update to 3.1.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 David Cantrell <dcantrell@redhat.com> - 3.1-4
- Use %%autosetup in %%prep

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 David Cantrell <dcantrell@redhat.com> - 3.1-1
- Upgrade to libjodycode-3.1
- Drop the forge macros because the project moved to an unsupported site

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 David Cantrell <dcantrell@redhat.com> - 3.0.1-1
- Upgrade to libjodycode-3.0.1

* Thu Jun 15 2023 David Cantrell <dcantrell@redhat.com> - 2.0.1-2
- Add a comment explaining Patch0 is for building and packaging on
  Fedora
- Use %%forgeautosetup macro in %%prep
- Do not package the static library
- Move the header file to the devel subpackage
- Do not use CFLAGS_EXTRA as that just duplicates the CFLAGS again

* Tue Jun 13 2023 David Cantrell <dcantrell@redhat.com> - 2.0.1-1
- Initial package
