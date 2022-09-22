%global shortcommit     225927b
%global compiledate     August\ 25,\ 2022

# https://github.com/zyedidia/micro
%global goipath         github.com/zyedidia/micro
Version:                2.0.11

%gometa -f

%global goname          micro

%global common_description %{expand:
Micro is a terminal-based text editor that aims to be easy to use and
intuitive, while also taking advantage of the full capabilities of modern
terminals. It comes as one single, batteries-included, static binary with no
dependencies, and you can download and use it right now.

As the name indicates, micro aims to be somewhat of a successor to the nano
editor by being easy to install and use in a pinch, but micro also aims to be
enjoyable to use full time, whether you work in the terminal because you prefer
it (like me), or because you need to (over ssh).}

%global golicenses      LICENSE LICENSE-THIRD-PARTY
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A modern and intuitive terminal-based text editor
# Upstream license specification: MIT and Apache-2.0
License:        MIT and ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%prep
%goprep
sed -i "s|github.com/zyedidia/json5|github.com/flynn/json5|" $(find . -name "*.go")

%build
export LDFLAGS="-X 'github.com/zyedidia/micro/internal/util.Version=%{version}' \
                -X 'github.com/zyedidia/micro/internal/util.CommitHash=%{shortcommit}' \
                -X 'github.com/zyedidia/micro/internal/util.CompileDate=%{compiledate}' \
                -X 'github.com/zyedidia/micro/internal/util.Debug=OFF'"

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%generate_buildrequires
%go_generate_buildrequires

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck -d cmd/micro/shellwords -d cmd/micro/terminfo

%files
%license LICENSE LICENSE-THIRD-PARTY
%doc README.md
%{_bindir}/*

%changelog
* Thu Aug 25 2022 Carl George <carl@george.computer> - 2.0.11-1
- Latest upstream, resolves rhbz#1960973
- Stop building on i686

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.0.8-6
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.8-5
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 15:04:32 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.8-1
- Update to 2.0.8 
- Close rhbz#1876359

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 19:33:22 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.6-1
- Update to 2.0.6 (#1849132)

* Thu Jun 18 21:23:31 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.4-1
- Update to 2.0.4 (#1823042)

* Mon Mar 02 21:28:04 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Feb 20 23:45:56 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-9
- Add util.Debug=OFF to LDFLAGS to disable debug functions

* Mon Feb 17 01:38:14 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.1-8
- Update to 2.0.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 23:24:56 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.1-6
- Update to new macros

* Wed Feb 20 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.1-5
- Fix sergi/go-diff BR

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.1-1
- Upstream release 1.4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-2
- Add missing versioning data to build stage
- Update to new Go packaging guidelines

* Fri Jan 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4.0-1
- Upstream release 1.4.0

* Thu Dec 07 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.4-1
- Upstream release 1.3.4

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.3-1
- Initial RPM release

