%bcond_without tests

Name:           adb-enhanced
Version:        2.12.0
Release:        %autorelease
Summary:        Tool for Android testing and development
License:        Apache-2.0
URL:            https://github.com/ashishb/adb-enhanced
Source0:        https://pypi.io/packages/source/a/adb-enhanced/adb_enhanced-%{version}.tar.gz
Source1:        remove-classpath.sh
Patch0:         remove-classpath-manifest.patch
BuildArch:      noarch
BuildRequires:  python3-devel


%description
ADB-Enhanced is a Swiss-army knife for Android testing and development. A
command-line interface to trigger various scenarios like screen rotation,
battery saver mode, data saver mode, doze mode, permission grant/revocation.

%prep
%autosetup -N -p1 -n adb_enhanced-%{version}
# Relax strict dependency pins (==) to >= to avoid build failures with newer system libraries
sed -i 's/==/>=/g' pyproject.toml

# Add missing [build-system] table to pyproject.toml so PEP 517 build works
cat >> pyproject.toml << 'EOF'

[build-system]
requires = ["setuptools>=61.0.0"]
build-backend = "setuptools.build_meta"
EOF

# Remove shebang from python libraries that are not directly executed
sed -i -e '1{\@^#!/usr/bin/env python3\?@d}' adbe/adb_enhanced.py adbe/main.py

# Remove Class-Path entry from the prebuilt jar manifest
bash %{SOURCE1} --extract
patch -p1 < %{PATCH0}
bash %{SOURCE1} --repack



%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l adbe

%if %{with tests}
%check
# the sdist does not ship the upstream tests/ tree, so only run the import smoke test
%pyproject_check_import
%endif

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/adbe

%changelog
%autochangelog
