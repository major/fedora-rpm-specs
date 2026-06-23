%bcond_with tests

Name:           adb-enhanced
Version:        2.10.0
Release:        %autorelease
Summary:        Tool for Android testing and development

License:        Apache-2.0
URL:            https://github.com/ashishb/adb-enhanced
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
ADB-Enhanced is a Swiss-army knife for Android testing and development. A
command-line interface to trigger various scenarios like screen rotation,
battery saver mode, data saver mode, doze mode, permission grant/revocation.

%prep
%autosetup
# Relax strict dependency pins (==) to >= to avoid build failures with newer system libraries
sed -i 's/==/>=/g' pyproject.toml

# Add missing [build-system] table to pyproject.toml so PEP 517 build works
cat >> pyproject.toml << 'EOF'

[build-system]
requires = ["setuptools>=61.0.0"]
build-backend = "setuptools.build_meta"
EOF

# Remove shebang from python libraries that are not directly executed
sed -i -e '1{\@^#!/usr/bin/env python@d}' adbe/adb_enhanced.py adbe/main.py

# Remove Class-Path entry from the prebuilt jar manifest to silence rpmlint warning
python3 -c "
import zipfile, os
jar_path = 'adbe/abe.jar'
with zipfile.ZipFile(jar_path, 'r') as z_in:
    with zipfile.ZipFile(jar_path + '.new', 'w') as z_out:
        for item in z_in.infolist():
            data = z_in.read(item.filename)
            if item.filename == 'META-INF/MANIFEST.MF':
                lines = [line for line in data.decode('utf-8').splitlines() if not line.startswith('Class-Path:')]
                data = '\n'.join(lines).encode('utf-8') + b'\n'
            z_out.writestr(item, data)
os.replace(jar_path + '.new', jar_path)
"



%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l adbe

%if %{with tests}
%check
%pyproject_check_import

%pytest -v tests/adbe_tests.py
%endif

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/adbe

%changelog
%autochangelog
