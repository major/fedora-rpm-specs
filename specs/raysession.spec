
Name:           raysession
Version:        0.17.2
Release:        4%{?dist}
Summary:        Session manager for audio software
License:        GPL-2.0-only
URL:            https://github.com/Houston4444/RaySession
Source0:        %{url}/releases/download/v%{version}/RaySession-%{version}-source.tar.gz
Source1:        README-wayland
Source2:        GPL-2
Source3:        qt6_app.1
BuildArch:      noarch

# Essential build dependencies
BuildRequires:  make
BuildRequires:  python3-pyqt6
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  help2man

# Essential runtime dependencies
Requires:       python3
Requires:       python3-alsa
Requires:       python3-pyliblo3
Requires:       python3-pyxdg
Requires:       python3-pyqt6
Requires:       python3-legacy-cgi
Requires:       hicolor-icon-theme
Requires:       shared-mime-info


%description
Ray Session is a GNU/Linux session manager for audio programs as Ardour,
Carla, QTractor, Non-Timeline, etc...

It uses the same API as Non Session Manager, so programs compatible with NSM
are also compatible with Ray Session. As Non Session Manager, the principle
is to load together audio programs, then be able to save or close all
documents together.

Ray Session offers a little more:

 - Factory templates for NSM and LASH compatible applications
 - Possibility to save any client as template
 - Save session as template
 - Name files with a prettier way
 - remember if client was started or not
 - Abort session almost anytime
 - Change Main Folder of sessions on GUI
 - Possibility to KILL client if clean exit is too long
 - Open Session Folder button (open default file manager)

Ray Session is being developed by houston4444, using Python3 and Qt5.


%prep
%autosetup -n RaySession-%{version}
cp %{SOURCE1} ./

%build
%set_build_flags
make LRELEASE=lrelease-qt6 %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

# Fix bash completion path
if [ -f "%{buildroot}%{_sysconfdir}/bash_completion.d/ray_completion.sh" ]; then
  sed -i 's|^PY_FILE=.*|PY_FILE=/usr/share/raysession/src/completion|' "%{buildroot}%{_sysconfdir}/bash_completion.d/ray_completion.sh"
  sed -i '1{/^#!/d}' "%{buildroot}%{_sysconfdir}/bash_completion.d/ray_completion.sh"
  chmod -x "%{buildroot}%{_sysconfdir}/bash_completion.d/ray_completion.sh" || true
fi

# Rewrite symlinks to remove the buildroot prefix
if [ -d "%{buildroot}" ]; then
  find "%{buildroot}" -type l | while read -r l; do
    tgt=$(readlink "$l" || true)
    case "$tgt" in
      "%{buildroot}"*)
        newt=${tgt#%{buildroot}}
        ln -nfs "$newt" "$l"
        ;;
    esac
  done
fi

# Remove empty files from the data tree
if [ -d "%{buildroot}%{_datadir}/%{name}" ]; then
  find "%{buildroot}%{_datadir}/%{name}" -type f -empty -delete || true
fi

# Make entry-point scripts executable; avoid chmod'ing library modules
if [ -d "%{buildroot}%{_bindir}" ]; then
  find "%{buildroot}%{_bindir}" -type f -exec grep -Il '^#!' '{}' ';' | xargs --no-run-if-empty chmod +x || true
fi
if [ -d "%{buildroot}%{_datadir}/%{name}/src/bin" ]; then
  find "%{buildroot}%{_datadir}/%{name}/src/bin" -type f -exec grep -Il '^#!' '{}' ';' | xargs --no-run-if-empty chmod +x || true
fi
if [ -d "%{buildroot}%{_datadir}/%{name}/data/bin" ]; then
  find "%{buildroot}%{_datadir}/%{name}/data/bin" -type f -exec grep -Il '^#!' '{}' ';' | xargs --no-run-if-empty chmod +x || true
fi

# Ensure packaged completion script is not executable
if [ -f "%{buildroot}%{_datadir}/%{name}/src/completion/ray_completion.sh" ]; then
  sed -i '1{/^#!/d}' "%{buildroot}%{_datadir}/%{name}/src/completion/ray_completion.sh"
  chmod -x "%{buildroot}%{_datadir}/%{name}/src/completion/ray_completion.sh" || true
fi

# Remove shebangs from Python modules (exclude bin paths)
if [ -d "%{buildroot}%{_datadir}/%{name}" ]; then
  find "%{buildroot}%{_datadir}/%{name}" -type f -name '*.py' \
    ! -path '*/src/bin/*' ! -path '*/data/bin/*' -exec sed -i '1{/^#!/d}' '{}' ';' || true
fi

# Correct common shebang typos in packaged bin scripts
if [ -d "%{buildroot}%{_datadir}/%{name}/src/bin" ]; then
  find "%{buildroot}%{_datadir}/%{name}/src/bin" -type f -exec sed -i 's|^#\!*/usr/bin env python3|#!/usr/bin/env python3|' '{}' ';' || true
fi

# Make session and jack config scripts executable when they have a shebang
for d in "%{buildroot}%{_datadir}/%{name}/session_scripts" "%{buildroot}%{_datadir}/%{name}/src/jack_config_script"; do
  if [ -d "$d" ]; then
    find "$d" -type f -exec grep -Il '^#!' '{}' ';' | xargs --no-run-if-empty chmod +x || true
  fi
done

# Remove compiled resource bytecode without source
find "%{buildroot}%{_datadir}/%{name}" -type f -name '*resources_rc*.pyc' -delete || true

# Remove Python bytecode and __pycache__ directories from packaged data
find "%{buildroot}%{_datadir}/%{name}" -type f -name '*.pyc' -delete || true
find "%{buildroot}%{_datadir}/%{name}" -type d -name '__pycache__' -exec rm -rf '{}' + || true

# Remove upstream hidden files
find "%{buildroot}%{_datadir}/%{name}" -type f \( -name '.directory' -o -name '.jack_config_script' \) -delete || true

# Install provided GPL-2 as the packaged COPYING
mkdir -p "%{buildroot}%{_datadir}/licenses/%{name}" || true
if [ -f "%{_sourcedir}/GPL-2" ]; then
  cp -p "%{_sourcedir}/GPL-2" "%{buildroot}%{_datadir}/licenses/%{name}/COPYING" || true
fi
if [ -f "%{buildroot}%{_datadir}/licenses/%{name}/COPYING" ]; then
  chmod 644 "%{buildroot}%{_datadir}/licenses/%{name}/COPYING" || true
fi

# Create /usr/bin symlinks for packaged data executables
if [ -d "%{buildroot}%{_datadir}/%{name}/src/bin" ]; then
  for f in $(cd "%{buildroot}%{_datadir}/%{name}/src/bin" && ls -1); do
    name=$(basename "$f")
    linkname=${name%%.*}
    if [ "$linkname" = "$name" ]; then
        ln -nfs ../share/%{name}/src/bin/"$f" "%{buildroot}%{_bindir}/$name" || true
    else
        ln -nfs ../share/%{name}/src/bin/"$f" "%{buildroot}%{_bindir}/$linkname" || true
    fi
  done
fi

mkdir -p "%{buildroot}%{_mandir}/man1"

# Generate manpages with help2man or fallback to minimal pages
if [ -d "%{buildroot}%{_bindir}" ]; then
  for f in $(cd "%{buildroot}%{_bindir}" && ls -1); do
    b=$(basename "$f")
    out="%{buildroot}%{_mandir}/man1/${b}.1"
    help2man -N -n "RaySession helper" -o "$out" "%{buildroot}%{_bindir}/$b" >/dev/null 2>&1 || true
  done
fi

# Add minimal manpage stubs for binaries that help2man can't document
MAN_STUBS="ray-daemon ray-jack_checker_daemon ray-jack_config_script ray-pulse2jack\
 ray_control ray_git raysession ray-alsapatch ray-jackpatch ray-network\
 ray-patch_dmn sooperlooper_nsm utility_script_keeper qt6_app"
for b in $MAN_STUBS; do
  out="%{buildroot}%{_mandir}/man1/${b}.1"
  if [ -x "%{buildroot}%{_bindir}/$b" ] && [ ! -f "$out" ]; then
    mkdir -p "%{buildroot}%{_mandir}/man1"
    cat > "$out" <<EOF
." Manpage for $b
.TH $b 1 "$(date +%Y-%m-%d)"
.SH NAME
$b \- helper for RaySession
.SH SYNOPSIS
.B $b
.SH DESCRIPTION
Minimal manpage stub for $b.
EOF
    gzip -n -f "$out" || true
  fi
done

# Ensure qt6_app has a manpage (some builds miss this one)
if [ -x "%{buildroot}%{_bindir}/qt6_app" ] && [ ! -f "%{buildroot}%{_mandir}/man1/qt6_app.1.gz" ]; then
  out="%{buildroot}%{_mandir}/man1/qt6_app.1"
  cat > "$out" <<EOF
." Manpage for qt6_app
.TH qt6_app 1 "$(date +%Y-%m-%d)"
.SH NAME
qt6_app \- helper for RaySession
.SH SYNOPSIS
.B qt6_app
.SH DESCRIPTION
Minimal manpage stub for qt6_app.
EOF
  gzip -n -f "$out" || true
fi

# Overwrite upstream COPYING with the provided GPL-2 so the packaged
# license is the canonical text
if [ -f "%{_sourcedir}/GPL-2" ] && [ -d "%{_builddir}/RaySession-%{version}" ]; then
  if [ -f "%{_builddir}/RaySession-%{version}/COPYING" ]; then
    cp -p "%{_sourcedir}/GPL-2" "%{_builddir}/RaySession-%{version}/COPYING" || true
    chmod 644 "%{_builddir}/RaySession-%{version}/COPYING" || true
  fi
fi

# If a manual page is provided in the sources, install it (fallback for qt6_app)
if [ -f "%{_sourcedir}/qt6_app.1" ]; then
  install -D -m 644 "%{_sourcedir}/qt6_app.1" "%{buildroot}%{_mandir}/man1/qt6_app.1" || true
  gzip -n -f "%{buildroot}%{_mandir}/man1/qt6_app.1" || true
fi

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop



%files
%doc README.md TODO TRANSLATORS
%license %{_datadir}/licenses/%{name}/COPYING
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%config(noreplace) %{_sysconfdir}/xdg/raysession/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/ray_completion.sh
%{_mandir}/man1/*

# Exclude duplicate upstream data that would be packaged twice
%exclude %{_datadir}/%{name}/data/share/applications/*
%exclude %{_datadir}/%{name}/manual/*
%exclude %{_datadir}/%{name}/HoustonPatchbay/manual/*
%exclude %{_datadir}/%{name}/HoustonPatchbay/themes/.directory
%exclude %{_datadir}/%{name}/manual/.directory
%exclude %{_datadir}/%{name}/session_templates/with_jack_config/ray-scripts/.directory
%exclude %{_datadir}/%{name}/session_templates/with_jack_config/ray-scripts/.jack_config_script
%exclude %{_datadir}/%{name}/HoustonPatchbay/source/patchbay/patchcanvas/xdg.py

%changelog
* Sat Jan 17 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.17.2-4
- Bump release to 4; include GPL-2 and qt6_app manpage

* Fri Jan 16 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.17.2-3
- Fix for missing dependency on python3-legacy-cgi

* Fri Jan 16 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.17.2-2
- Fix for incorrect package name (Bug #2430438)

* Sat Jan 10 2026 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.17.2-1
- New upstream release
- Removed patches, fixed upstream

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.14.3-5
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.14.3-4
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Adam Williamson <awilliam@redhat.com> - 0.14.3-1
- New release 0.14.3
- Patch to work with pyliblo3 (for F41+ / Python 3.13+)

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.1-12
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.9.1-1
- Removed patches, issues were fixed upstream
- CLI: Control almost all GUI actions and more with the CLI ray_control.
- Session scripts: allow user to edit shell scripts at session load, save and
  close.
- JACK config session script: script that saves and recalls the JACK
  configuration for the session.
- Add this from session templates in "New Session" window.
- RayHack: New client protocol which is an alternative to ray-proxy.
- This allows to launch directly the process and to edit its properties even if
  process is stopped.
- Obviously NSM protocol is highly preferred, this protocol is a workaround
  only, nothing more.
- Factory client templates are installed in /etc/xdg/raysession to allow
  packagers to add some templates.
- Always prefer NSM template if NSM compatibility is found in executable binary
- Get client label, icon and description from their .desktop file
- Subfolder combobox removed in New Session Dialog
- Daemon option "Save from client" has been removed. Please affect a global
  keyboard shortcut (Meta+Ctrl+S) to ray_control save instead.

* Sat Feb 8 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.8.3-1
- Initial release for Fedora
