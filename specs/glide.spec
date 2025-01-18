# Run tests in check section
%bcond_without check

# https://github.com/Masterminds/glide
%global goipath         github.com/Masterminds/glide
Version:                0.13.2

%gometa

%global common_description %{expand:
Glide is a tool for managing the vendor directory within a Go package. This
feature, first introduced in Go 1.5, allows each package to have a vendor
directory containing dependent packages for the project. These vendor packages
can be installed by a tool (e.g. glide), similar to go get or they can be
vendored and distributed with the package.}

%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md README.md

Name:           glide
Release:        19%{?dist}
Summary:        Package Management for Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
# From https://github.com/mattfarina/glide-hash/blob/master/main.go
Patch0:         Add-glide-hash.patch

# glide.go
BuildRequires:  golang(github.com/codegangsta/cli)

# Remaining dependencies not included in main packages
BuildRequires:  golang(github.com/Masterminds/semver) < 2.0.0
BuildRequires:  golang(github.com/Masterminds/vcs)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1

%build
%gobuild -o %{gobuilddir}/bin/glide %{goipath}
%gobuild -o %{gobuilddir}/bin/glide-hash %{goipath}/glide-hash

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
# Disabled tests need vendoring
%check
%gocheck -d dependency -d path -d util
%endif

%files
%license LICENSE
%doc docs CHANGELOG.md README.md
%{_bindir}/glide
%{_bindir}/glide-hash

%gopkgfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0.13.2-17
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.13.2-11
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.13.2-10
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.2-2
- Update to latest Go macros
- Enable some tests

* Wed Apr 03 00:52:40 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.13.2-1
- Release 0.13.2 (#1694353)

* Sun Feb 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.1-6
- Fix broken version specification

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org>
- 0.13.1-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.13.1-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.13.1-1
- Update to v0.13.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.5.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.4.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.3.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-0.2.git8032c28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git8032c28
- First package for Fedora
  resolves: #1373623
