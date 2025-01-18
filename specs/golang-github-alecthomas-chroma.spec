# https://github.com/alecthomas/chroma
%global goipath         github.com/alecthomas/chroma
Version:                0.10.0

%gometa

%global common_description %{expand:
Chroma takes source code and other structured text and converts it into syntax
highlighted HTML, ANSI-coloured text, etc.

Chroma is based heavily on Pygments, and includes translators for Pygments
lexers and styles.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Release:        12%{?dist}
Summary:        General purpose syntax highlighter in pure Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license COPYING
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 0.10.0-10
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 0.10.0-4
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.0-3
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 15 2022 Maxwell G <gotmax@e.email> - 0.10.0-1
- Update to 0.10.0. Fixes rhbz#1973059.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 15:51:52 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.1-1
- Update to 0.9.1
- Close: rhbz#1953303

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.2-1
- Update to 0.8.2
- Close: rhbz#1880976

* Sat Aug 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.8.0-1
- Update to latest revision

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.3-1
- Update to latest revision
- Use generated dynamic buildrequires

* Sat May 02 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.2-1
- Update to latest revision

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 19:46:31 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.1-1
- Update to 0.7.1

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- Update to latest version

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.9-1
- Update to latest version

* Thu Oct 31 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.8-1
- Update to latest version

* Thu Oct 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.7-1
- Update to latest version

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.6-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 17:48:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.3-2
- Update to new macros

* Wed Apr 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-1
- Update to latest version

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.2-1
- Update to latest version
- Rewrite spec using new Go macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7.20171017git03b0c0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6.20171017git03b0c0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5.20171017git03b0c0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-4.20171017git03b0c0d
- Disabling check until github.com/alecthomas/assert hits rawhide

* Sat Oct 21 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-3.20171017git03b0c0d
- Update to latest revision

* Sat Oct 14 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-2
- Fix build paths for exercise and css2style
- Add BR for gopkg.in/alecthomas/kingpin.v3
- Do not build bin files until kingpin v3 is released

* Wed Oct 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.1.1-1
- First package for Fedora
