# Generated by go2rpm
%bcond_without check

# https://github.com/ulikunitz/xz
%global goipath         github.com/ulikunitz/xz
Version:                0.5.11

%gometa

%global common_description %{expand:
This Go language package supports the reading and writing of xz compressed
streams. It includes also a gxz command for compressing and decompressing data.
The package is completely written in Go and doesn't have any dependency on any C
code.}

%global golicenses      LICENSE
%global godocs          doc README.md TODO.md

Name:           %{goname}
Release:        10%{?dist}
Summary:        Pure golang package for reading and writing xz-compressed files

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mv %{gobuilddir}/bin/xb %{gobuilddir}/bin/goxb

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc doc README.md TODO.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.11-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0.5.11-6
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Dominik Mierzejewski <dominik@greysector.net> - 0.5.11-1
- update to 0.5.11 (#2152794)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.5.10-5
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.10-4
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 20 2021 Dominik Mierzejewski <dominik@greysector.net> - 0.5.10-1
- update to 0.5.10 (#1924347)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 23:23:36 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.9-1
- Update to 0.5.9
- Close: rhbz#1908938

* Thu Aug 20 2020 Dominik Mierzejewski <dominik@greysector.net> - 0.5.8-1
- Release 0.5.8 (#1870433)
- fixes CVE-2020-16845

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 09 2020 Dominik Mierzejewski <dominik@greysector.net> - 0.5.7-1
- update to 0.5.7 (#1806448)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 18:41:46 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.5.6-1
- Release 0.5.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.5.4-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5.4-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.5.4-1
- initial package for Fedora
