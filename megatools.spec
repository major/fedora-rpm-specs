%global snapshot 20220519

Name:           megatools
Version:        1.11.0
Release:        7%{?dist}
Summary:        Command line client for MEGA
License:        GPLv3+
URL:            http://megatools.megous.com/
Source0:        http://megatools.megous.com/builds/builds/%{name}-%{version}.%{snapshot}.tar.gz
Source1:        http://megatools.megous.com/builds/builds/%{name}-%{version}.%{snapshot}.tar.gz.asc
Source2:        %{name}.rpmlintrc

BuildRequires:  asciidoc
BuildRequires:  docbook2X
BuildRequires:  meson
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)

%description
Megatools is a collection of programs for accessing Mega service from a command
line of your desktop or server.

Megatools allow you to copy individual files as well as entire directory trees
to and from the cloud. You can also perform streaming downloads for example to
preview videos and audio files, without needing to download the entire file.

You can register an account using a "megareg" tool, with the benefit of having
true control of your encryption keys.

Megatools are robust and optimized for fast operation - as fast as Mega servers
allow. Memory requirements and CPU utilization are kept at minimum.

%prep
%autosetup -n %{name}-%{version}.%{snapshot}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license LICENSE
%doc NEWS README TODO LICENSE
%{_bindir}/mega*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.11.0-6
- Upstream release rhbz#2088522

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.11.0-4
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 05 2021 Gerald Cox <gbcox@fedoraproject.org> - 1.11.0-1
- Upstream release rhbz#1912616

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Gerald Cox <gbcox@fedoraproject.org> - 1.10.3-1
- Upstream release rhbz#1824110

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.10.2-1
- Upstream release rhbz#1610323

* Fri Jul 27 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.10.1-1
- Upstream release rhbz#1609261

* Wed Jul 25 2018 Simone Caronni <negativo17@gmail.com> - 1.10.0-2
- Add bash-completion support.

* Sun Jul 22 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.10.0-1
- Upstream release rhbz#1603054

* Thu Jul 19 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.10.0-0.2
- Upstream release rhbz#1603054

* Wed Jul 18 2018 Gerald Cox <gbcox@fedoraproject.org> - 1.10.0-0.1
- Upstream release rhbz#1603054

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.99git-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Simone Caronni <negativo17@gmail.com> - 1.9.99git-1
- Update to 1.9.99git.

* Fri Jun 29 2018 Simone Caronni <negativo17@gmail.com> - 1.9.98-6
- Clean up SPEC file.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 5 2016 Gerald Cox <gbcox@fedoraproject.org> 1.9.98-1
- Upstream release rhbz#1391793

* Tue Feb 2 2016 Gerald Cox <gbcox@fedoraproject.org> - 1.9.97-1
- Upstream release rhbz#1304133

* Sat Jan 2 2016 Gerald Cox <gbcox@fedoraproject.org> - 1.9.96-1
- Upstream release rhbz#1295096

* Mon Jun 15 2015 Gerald Cox <gbcox@fedoraproject.org> - 1.9.95-4
- Implement recommendations from rhbz#1228924 comment 8.

* Mon Jun 15 2015 Gerald Cox <gbcox@fedoraproject.org> - 1.9.95-3
- Implement recommendations from rhbz#1228924 comment 6.

* Fri Jun 12 2015 Gerald Cox <gbcox@fedoraproject.org> - 1.9.95-2
- Implement recommendations from rhbz#1228924 comment 2.

* Tue May 26 2015 Gerald Cox <gbcox@fedoraproject.org> - 1.9.95-1
- Initial release
