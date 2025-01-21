%global commit      5a1c8d83ba1514ca8d045ba80403f93772fb371a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        2020704

%bcond_without  tests

Name:           the_silver_searcher
Version:        2.2.0^%{date}.%{shortcommit}
Release:        12%{?dist}
Summary:        Super-fast text searching tool (ag)
# The bundled copy of src/uthash.h is BSD-1-Clause, but we remove that in
# %%prep so this package is only Apache-2.0.
License:        Apache-2.0
URL:            https://github.com/ggreer/the_silver_searcher
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# https://github.com/ggreer/the_silver_searcher/pull/1145
Patch:          0001-update-zsh-completion-for-new-options.patch
# https://github.com/ggreer/the_silver_searcher/pull/1410
Patch:          0002-Install-shell-completion-files-to-correct-locations.patch
# https://github.com/ggreer/the_silver_searcher/pull/1540
Patch:          0003-bash-completion-port-to-v2-API.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  uthash-devel
%if %{with tests}
BuildRequires:  python3-cram
BuildRequires:  git-core
%endif

Provides:       ag


%description
The Silver Searcher is a code searching tool similar to ack,
with a focus on speed.


%prep
%autosetup -n %{name}-%{commit} -p 1

# https://github.com/ggreer/the_silver_searcher/issues/1411
rm src/uthash.h
sed -e '/ag_SOURCES/ s/ src\/uthash.h//' -i Makefile.am


%build
aclocal
autoconf
autoheader
automake --add-missing
%configure --disable-silent-rules
%make_build


%install
%make_install


%if %{with tests}
%check
make test
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/ag
%{_mandir}/man1/ag.1*
%{_datadir}/bash-completion/completions/ag
%{_datadir}/zsh/site-functions/_ag


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 31 2024 Carl George <carlwgeorge@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-11
- Add patch to fix bash completion rhbz#2322963
- Correct license to Apache-2.0

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0^2020704.5a1c8d8-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Björn Esser <besser82@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-3
- Rebuild(uthash)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0^2020704.5a1c8d8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Carl George <carl@george.computer> - 2.2.0^2020704.5a1c8d8-1
- Switch to caret versioning
- Build against system uthash
- Add patch for zsh completion of new flags

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Carl George <carl@george.computer> - 2.2.0-3.2020704git5a1c8d8
- Update to latest upstream commit
- Add patch to use correct shell completion locations
- Run test suite
- Add provides for ag and bundled uthash

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Shlomi Fish <shlomif@cpan.org> - 2.2.0-1
- New upstream version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 6 2017 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 2.1.0-1
- update to 2.1.0

* Fri Jun 9 2017 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 2.0.0-1
- update to 2.0.0

* Thu Nov 3 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.33.0-1
- update to 1.0.2

* Thu Nov 3 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.33.0-1
- update to 0.33.0

* Thu Sep 22 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.32.0-3
- Fixed bz#1377596

* Thu Jun 30 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.32.0-1
- update to 0.32.0

* Sun Jan 24 2016 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.31.0-2
- Build for RHEL6(EPEL)

* Tue Dec 29 2015 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.31.0-1
- update to 0.31.0

* Thu May 07 2015 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.30.0-1
- update to 0.30.0

* Mon Dec 15 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.27.0-1
- update to 0.27.0

* Mon Nov 03 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.26.0-1
- update to 0.26.0

* Wed Oct 15 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.25.0-1
- update to 0.25.0

* Tue Sep 30 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.24.1-1
- update to 0.24.1

* Sun Jun 22 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.22.0-1
- update to 0.22.0

* Tue Apr 22 2014 Kenjiro Nakayama <nakayamakenjiro@gmail.com> - 0.21.0-1
- update to 0.21.0

* Thu Sep 12 2013 Henrik Hodne <henrik@hodne.io> - 0.16-2
- Initial RPM release
