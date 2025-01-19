Name: pasdoc
Summary: Documentation tool for Pascal and Object Pascal source code

# The readme says simply "GNU GPL 2", but license headers in code files
# say "version 2 of the License, or (at your option) any later version".
License: GPL-2.0-or-later

%global with_gui 1
%global with_tools 1
%global with_tests 1

Version: 0.16.0
Release: 13%{?dist}

URL: https://github.com/pasdoc/pasdoc
Source0: %{URL}/archive/v%{version}/pasdoc-%{version}.tar.gz

# Submitted upstream: https://github.com/pasdoc/pasdoc/pull/135
Source10: %{name}.man
Source20: pascal_pre_proc.man
Source21: file_to_pascal_data.man

Source30: %{name}-gui.desktop
Source31: %{name}-gui.metainfo.xml

# The test runner script always rebuilds the program from scratch
# before actually performing any tests.
Patch0: 0000-adapt-test-runner.patch

# Edit the project configuration files to enable DWARF3 debuginfo
Patch1: 0001-enable-dwarf3-debuginfo.patch

ExclusiveArch: %{fpc_arches}

BuildRequires: fpc

%if 0%{?with_gui}
%global widgetset gtk2
BuildRequires: desktop-file-utils
BuildRequires: lazarus-lcl-%{widgetset}
BuildRequires: lazarus-tools
BuildRequires: libappstream-glib
%endif

%if 0%{?with_tests}
BuildRequires: make
BuildRequires: %{_bindir}/diff
BuildRequires: %{_bindir}/xmllint
%endif


%description
PasDoc is a documentation tool for Pascal and Object Pascal source code.
Documentation is generated from comments found in the source code, or from
external files. Numerous formatting @-tags are supported. Many output formats
are supported, including HTML and LaTeX.


%if 0%{?with_gui}
%package gui
Summary: Graphical user interface for the PasDoc documentation generator
Requires: hicolor-icon-theme

%description gui
PasDoc is a documentation tool for Pascal and Object Pascal source code.

This package provides a graphical user interface for PasDoc, allowing to
generate documentation files from previously annotated source code.
%endif


%if 0%{?with_tools}
%package tools
Summary: Helper tools for PasDoc

%description tools
Helper tools useful for analyzing Pascal code
and embedding files (both text and binary) inside Pascal sources.
%endif


%prep
%autosetup -p1


%build
# The upsteam source contains a Makefile, but it sets many compiler options
# such as range checking code, optimization level, and so on.
#
# Instead of using the Makefile, let's compile manually,
# so that Fedora's default settings for FPC are applied.
mkdir -p build/bin build/obj
%global fpc_flags -g -gl -gw3 -O3 -Mobjfpc -Sh -FE./build/bin -FU./build/obj

fpc %{fpc_flags} \
	-Fu./source/component \
	-Fu./source/component/tipue \
	-Fu./source/console \
	-Fi./source/component \
	-Fi./source/component/images \
	./source/console/pasdoc.dpr

# Build the unit test app
%if 0%{?with_tests}
	fpc %{fpc_flags} "./tests/fpcunit/test_pasdoc.lpr"
	mv ./build/bin/test_pasdoc ./tests/
%endif

# Build the helper tools
%if 0%{?with_tools}
	for TOOL in pascal_pre_proc file_to_pascal_data file_to_pascal_string; do
		fpc %{fpc_flags} "./source/tools/${TOOL}.dpr"
	done
%endif

# Build the gui
%if 0%{?with_gui}
	lazbuild --add-package-link ./source/packages/lazarus/pasdoc_package.lpk
	lazbuild --widgetset=%{widgetset} --recursive ./source/gui/pasdoc_gui.lpi
%endif


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} ./build/bin/*

MANDIR="%{buildroot}%{_mandir}/man1"
install -m 755 -d "${MANDIR}"
install -m 644 -p '%{SOURCE10}' "${MANDIR}/%{name}.1"

# Install man pages for tools.
# file_to_pascal_data and file_to_pascal_string are almost the same,
# so the single man page covers them both.
%if 0%{?with_tools}
install -m 644 -p '%{SOURCE20}' "${MANDIR}/pascal_pre_proc.1"
install -m 644 -p '%{SOURCE21}' "${MANDIR}/file_to_pascal_data.1"
ln -sr "${MANDIR}"/file_to_pascal_{data,string}.1
%endif

%if 0%{?with_gui}
install -m 755 ./source/gui/pasdoc_gui %{buildroot}%{_bindir}/%{name}-gui

for SIZE in 16 32 64 128 256; do
	# Icon files use zero-padded three-digit numbers in their names
	PADSIZ="$(printf '%%03d' "${SIZE}")"
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps"

	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p \
		"./source/gui/icons/PasDoc${PADSIZ}.png" \
		"${ICON_DIR}/%{name}-gui.png"
done

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p -t %{buildroot}%{_datadir}/applications '%{SOURCE30}'

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p -t %{buildroot}%{_metainfodir} '%{SOURCE31}'
%endif


%check
%if 0%{?with_tests}
export PASDOC_BIN="$(pwd)/build/bin/pasdoc"
export USE_DIFF_TO_COMPARE="true"

cd tests/
./test_pasdoc -a
./run_all_tests.sh
%endif

%if 0%{?with_gui}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}-gui.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
%endif


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%if 0%{?with_tools}
%files tools
%license LICENSE
%{_bindir}/file_to_pascal_data
%{_bindir}/file_to_pascal_string
%{_bindir}/pascal_pre_proc
%{_mandir}/man1/file_to_pascal_data.1*
%{_mandir}/man1/file_to_pascal_string.1*
%{_mandir}/man1/pascal_pre_proc.1*
%endif

%if 0%{?with_gui}
%files gui
%doc source/gui/HISTORY
%doc source/gui/README
%doc source/gui/TODO
%license LICENSE
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-gui.png
%{_metainfodir}/%{name}-gui.metainfo.xml
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.0-8
- BuildRequire only chosen Lazarus sub-packages
- Add missing BuildRequires on "make"
- Convert License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.0-4
- Fix license tag (GPLv2 -> GPLv2-or-later)
- Generate DWARF3 debuginfo instead of DWARF2
- Don't install the 512px icon (upstream lied, it's actually 480px)
- Add an AppStream metainfo file for the GUI

* Sun Nov 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.0-3
- Add man pages for all the executables (apart from the gui)
- Don't require the main package in gui subpackage
  (the GUI is an independent program, not just a frontend for the console)
- Move the tools to a separate subpackage (not required by pasdoc to run)
- Preserve timestamps when installing files
- Add %%doc files to the gui subpackage

* Tue Sep 21 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.0-2
- Build the GUI (as a sub-package)
- Build and run the test suite

* Wed Sep 15 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.16.0-1
- Initial packaging
