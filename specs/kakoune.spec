%if 0%{?fedora} <= 39
# Disable LTO due regression in GCC
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=114501
%global _lto_cflags %nil
%endif

%bcond_without tests

Name:           kakoune
Version:        2024.05.18
Release:        3%{?dist}
Summary:        Code editor heavily inspired by Vim

License:        Unlicense
URL:            https://kakoune.org/
Source0:        https://github.com/mawww/kakoune/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gcc-c++ >= 10.3
BuildRequires:  glibc-langpack-en
BuildRequires:  make

BuildRequires:  pkgconfig(ncurses) >= 5.3

%description
Features:

  * Multiple selections
  * Customization
  * Text editing tools
  * Client/Server architecture
  * Advanced text manipulation primitives
  * Active development & support

Kakoune is a code editor that implements Vi’s "keystrokes as a text editing
language" model. As it is also a modal editor, it is somewhat similar to the
Vim editor (after which Kakoune was originally inspired).

Kakoune can operate in two modes: normal and insertion. In insertion mode,
keys are directly inserted into the current buffer. In normal mode, keys are
used to manipulate the current selection and to enter insertion mode.

Kakoune has a strong focus on interactivity. Most commands provide immediate
and incremental results, while being competitive with Vim in terms of
keystroke count.

Kakoune works on selections, which are oriented, inclusive ranges of
characters. Selections have an anchor and a cursor. Most commands move both of
them except when extending selections, where the anchor character stays fixed
and the cursor moves around.


%prep
%autosetup -p1

# Use default Fedora build flags
sed -i '/CXXFLAGS-debug-no = -O3 -g3/d' Makefile


%build
%set_build_flags
%make_build


%install
%make_install \
    PREFIX=%{_prefix} \
    version=%{version} \
    docdir=%{buildroot}%{_docdir}/%{name} \
    %{nil}


%if %{with tests}
%check
%set_build_flags
LANG=en_US.utf8 %make_build test
%endif


%files
%license UNLICENSE
%doc README.asciidoc CONTRIBUTING VIMTOKAK doc/pages/changelog.asciidoc
%{_bindir}/kak
%{_datadir}/kak/
%{_libexecdir}/kak/
%{_mandir}/man1/*.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.05.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.05.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 18 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 2024.05.18-1
- chore: Update to 2024.05.18

* Thu May 09 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 2024.05.09-2
- build: Disable LTO due regression in GCC. For f38, f39 only.

* Thu May 09 2024 Artem Polishchuk <ego.cordatus@gmail.com> - 2024.05.09-1
- chore: Update to 2024.05.09

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.08.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.08.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 02 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 2023.08.05-1
- chore: Update to 2023.08.05 (rh#2229464)

* Sat Jul 29 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 2023.07.29-1
- chore: Update to 2023.07.29

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.10.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Artem Polishchuk <ego.cordatus@gmail.com> - 2022.10.31-4
- build: Add upstream patch with GCC 13 fix | #2171582

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.10.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2022.10.31-2
- build: v2022.10.31 requires GCC >= 10.3

* Mon Oct 31 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2022.10.31-1
- chore: Update to 2022.10.31

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.11.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 12 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2021.11.08-3
- fix: Add upstream patch "Make Color::validate_alpha() a constexpr function"
  Fix FTBFS 36

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.11.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 07 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2021.11.08-1
- chore(update): 2021.11.08

* Thu Oct 28 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2021.10.28-1
- chore(update): 2021.10.28

* Sat Aug 28 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2021.08.28-1
- build(update): 2021.08.28

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.09.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.09.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Jeff Law <law@gmail.com> - 2020.09.01-1
- Fix missing #includes for gcc-11

* Tue Sep  1 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2020.09.01-1
- Update to 2020.09.01

* Tue Aug 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2020.08.04-1
- Update to 2020.08.04

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.01.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.01.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2020.01.16-2
- Add version information during build

* Thu Jan 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2020.01.16-1
- Update to 2020.01.16

* Tue Dec 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2019.12.10-1
- Update to 2019.12.10

* Tue Nov 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2019.07.01-4
- Add patch to pass tests with default Fedora build flags

* Fri Nov 22 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2019.07.01-2
- Packaging fixes

* Wed Apr 24 2019 Jiri Konecny <jkonecny@redhat.com> - v2019.01.20-1
- Add a new build dependency (glibc-langpack-en) required for Fedora 30 and later
- Update version

* Fri Oct 12 2018 Jiri Konecny <jkonecny@redhat.com> - v2018.09.04-1
- Update spec file to a new release

* Sat May 5 2018 Łukasz Jendrysik <scadu@disroot.org> - v2018.04.13
- Use tagged release

* Wed May 11 2016 jkonecny <jkonecny@redhat.com> - 0-208.20160511git84f62e6f
- Add LANG=en_US.UTF-8 to fix tests
- Update to git: 84f62e6f

* Thu Feb 11 2016 jkonecny <jkonecny@redhat.com> - 0-158.20160210git050484eb
- Add new build requires asciidoc
- Use new man pages

* Sat Mar 28 2015 jkonecny <jkonecny@redhat.com> - 0-5.20150328gitd1b81c8f
- Automated git update by dgroc script new hash: d1b81c8f

* Tue Mar 24 2015 Jiri Konecny <jkonecny@redhat.com> 0-1.7eaa697git
- Add tests

* Tue Mar 17 2015 Jiri Konecny <jkonecny@redhat.com> 0-1.12a732dgit
- Create first rpm for kakoune
