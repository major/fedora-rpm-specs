Summary: Strong GPG verification of git tags
Name: git-evtag
Version: 2016.1
Release: 28%{?dist}

License: LGPLv2+
#VCS: https://github.com/cgwalters/git-evtag
URL: https://github.com/cgwalters/git-evtag
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc

# We always run autogen.sh
BuildRequires: autoconf automake libtool

BuildRequires: pkgconfig(libgit2)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: make

Requires: git
Requires: gnupg2

%description
git-evtag wraps "git tag" functionality, adding stronger checksums
that cover the complete content.

%prep
%autosetup

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules
%make_build

%install
%make_install INSTALL="install -p"

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Pete Walter <pwalter@fedoraproject.org> - 2016.1-27
- Rebuild for libgit2 1.6.x

* Fri Jan 27 2023 Pete Walter <pwalter@fedoraproject.org> - 2016.1-26
- Rebuild for libgit2 1.5.x

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 09 2022 Pete Walter <pwalter@fedoraproject.org> - 2016.1-24
- Rebuild for libgit2 1.4.x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Igor Raits <igor.raits@gmail.com> - 2016.1-22
- Rebuild for libgit2 1.4.x

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2016.1-20
- Rebuild against libgit2 1.3.x

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 20:30:33 CET 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2016.1-17
- Rebuild against libgit2 1.1.x

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2016.1-14
- Rebuild for libgit2 1.0.0

* Tue Mar 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2016.1-13
- Rebuild for libgit2 0.99

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2016.1-10
- Rebuild for libgit2 0.28.x

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2016.1-8
- Rebuild for libgit2 0.27.x

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 2016.1-3
- Rebuild for libgit2 0.26.x

* Tue Jan 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 2016.1-2
- Rebuild for libgit2-0.25.x

* Sun Nov 20 2016 Colin Walters <walters@verbum.org> - 2016.1-1
- Initial package
