%bcond_without check

%global _hardened_build 1

# https://github.com/shuLhan/go-bindata
%global goipath         github.com/shuLhan/go-bindata
Version:                3.6.1

%gometa

%global common_description %{expand:
A small utility which generates Go code from any file. Useful for embedding
binary data in a Go program.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md CHANGELOG

Name:           %{goname}
Release:        16%{?dist}
Summary:        A small utility which generates Go code from any file

# Upstream license specification: CC0-1.0
# Automatically converted from old format: CC0 - review is highly recommended.
License:        CC0-1.0
URL:            %{gourl}
Source0:        %{gosource}

Patch0:         0001-Fixes-for-possible-formatting-directive-and-extra-ne.patch

BuildRequires:  help2man

%description
%{common_description}

%gopkg

%prep
%goprep
# https://github.com/shuLhan/go-bindata/pull/47
%patch -P0 -p1

%build
%gobuild -o %{gobuilddir}/bin/go-bindata.shulhan %{goipath}/cmd/go-bindata
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{summary}" -s 1 -o %{gobuilddir}/share/man/man1/go-bindata.shulhan.1 -N --version-string="%{version}" %{gobuilddir}/bin/go-bindata.shulhan

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc AUTHORS CONTRIBUTING.md README.md CHANGELOG
%{_mandir}/man1/go-bindata.shulhan.1*
%{_bindir}/*

%gopkgfiles

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.6.1-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 3.6.1-13
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 3.6.1-7
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.6.1-6
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Tue Jan 25 2022 Brandon Perkins <bperkins@redhat.com> - 3.6.1-5
- Patch for possible formatting directive and extra newline errors in tests
- Close: rhbz#2045613

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Brandon Perkins <bperkins@redhat.com> - 3.6.1-1
- Update to version 3.6.1 (Fixes rhbz#1874216)

* Mon Aug 03 2020 Brandon Perkins <bperkins@redhat.com> - 3.6.0-2
- Rename binary to go-bindata.shulhan so it does not conflict with go-bindata

* Sun Aug 02 2020 Brandon Perkins <bperkins@redhat.com> - 3.6.0-1
- Initial package (Fixes rhbz#1862861)
