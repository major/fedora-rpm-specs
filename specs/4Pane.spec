# Multiple files refers to the name "4Pane", not "4pane", so
# let's use 4Pane as %%{name}

# Explicitly declare this, as this package
# really expects this
# (expanded afterwards, use %%define)
%define	_docdir_fmt	%{NAME}

Name:			4Pane
Version:		8.0
Release:		12%{?dist}
Summary:		Multi-pane, detailed-list file manager

# Overall		GPL-3.0-only
# 4Pane.appdata.xml	CC0-1.0
# Accelerators.cpp and etc		LGPL-2.0-or-later (wxWindows)
# sdk/bzip/LICENSE	bzip2-1.0.6 (unused)
# SPDX confirmed
License:		GPL-3.0-only AND LGPL-2.0-or-later AND CC0-1.0
URL:			http://www.4pane.co.uk/
Source0:		http://downloads.sourceforge.net/fourpane/4pane-%{version}.tar.gz
# https://sourceforge.net/p/fourpane/bugs/22/
# https://sourceforge.net/p/fourpane/git4pane/ci/d8b74e4df86fb526ee9caad284b9eb3efe528ac5/
# Make files under /tmp unpredictable
Patch0:		4Pane-d8b74e4-tmp-file-name.patch

BuildRequires:	gcc-c++
BuildRequires:	bzip2-devel
BuildRequires:	xz-devel
BuildRequires:	wxGTK-devel
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  /usr/bin/appstream-util
BuildRequires:	gettext
BuildRequires:	git
BuildRequires:	make

%description
4Pane is a multi-pane, detailed-list file manager. It is designed
to be fully-featured without bloat, and aims for speed rather than
visual effects.
In addition to standard file manager things, it offers multiple
undo and redo of most operations (including deletions), archive
management including 'virtual browsing' inside archives, multiple
renaming/duplication of files, a terminal emulator and user-defined
tools.

%prep
%setup -q -n 4pane-%{version}
%patch -P0 -p1 -b .tmpfile

%if 0
cat > .gitignore <<EOF
configure
config.guess
config.sub
aclocal.m4
config.h.in
EOF

git init
git config user.email "4Pane-maintainers@fedoraproject.org"
git config user.name "4Pane owners"
git add .
git commit -m "base" -q
%endif

sed -i.cflags configure \
	-e '\@[ \t]\{5,\}C.*FLAGS[ \t]*=[ \t]*$@d'

%build
export WX_CONFIG_NAME=$(ls -1 %{_bindir}/wx-config-3.* | sort | tail -n 1)
export EXTRA_CXXFLAGS="%{optflags}"

# --without-builtin_bzip2 means using system bzip2
%configure\
	--disable-desktop \
	--without-builtin_bzip2 || \
	{ sleep 5 ; cat config.log ; sleep 10 ; exit 1; }
%make_build

%install
%make_install

# Some manual installation
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,32x32}/apps

install -cpm 644 rc/%{name}.desktop %{buildroot}%{_datadir}/applications/
install -cpm 644 bitmaps/%{name}Icon32.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
install -cpm 644 bitmaps/%{name}Icon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_mandir}/man1
install -cpm 644 4Pane.1 %{buildroot}%{_mandir}/man1/

%find_lang %{name}

# Once remove document and let %%doc re-install them
rm -rf %{buildroot}%{_docdir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files -f %{name}.lang
%license	LICENCE
%doc	doc/*
%doc	README
%doc	changelog

%{_bindir}/4pane
%{_bindir}/%{name}

%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/%{name}.appdata.xml

%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0-10
- Upstream fix to make files under /tmp unpredictable

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0-8
- SPDX migration

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.0-2
- 8.0

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 7.0-6
- Rebuild with wxWidgets 3.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.0-1
- 7.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2010 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.0-1
- 6.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0-1
- 5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0-2
- Patch from the upstream to fix sizing and color issue with
  GTK 3.20 (bug 1345924)

* Thu Apr 07 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0-1
- 4.0
- Enable hardened build again

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0-7
- Kill hardened build, does not build

* Mon Dec 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0-6
- Patch for toolbar issue, requested by the upstream

* Sun Dec 21 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0-5
- Add man page, appdata (on F-21+)

* Thu Dec 11 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0-3
- Replace Patch0 with the one revised by the upstream

* Wed Dec 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0-2
- Patch to fix crash with managing bookmark on non-English
  locale (sourceforge 767206)

* Tue Dec  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0-1
- Initial package
