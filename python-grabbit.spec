Name:           python-grabbit
Version:        0.2.6
Release:        %autorelease
Summary:        Get grabby with file trees

# The bundled grabbit/external/inflect.py is GPLv3+, but we remove it.
License:        MIT
URL:            https://github.com/grabbles/grabbit
Source0:        %{url}/archive/%{version}/grabbit-%{version}.tar.gz

# Update versioneer from 0.18 to 0.21
# Fixes Python 3.11 compatiblity (RHBZ#2026767)
# https://github.com/grabbles/grabbit/pull/93
Patch0:         %{url}/pull/93.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand: \
Grabbit is a lightweight Python package for simple queries over filenames
within a project. It is geared towards projects or applications with highly
structured filenames that allow useful queries to be performed without having
to inspect the file metadata or contents.
}

%description
%{_description}


%package -n python3-grabbit
Summary:        %{summary}

%description -n python3-grabbit
%{_description}


%prep
%autosetup -n grabbit-%{version} -p1

# Unbundle inflect and six
for bundled in 'inflect' 'six'
do
  cat > "grabbit/external/${bundled}.py" <<EOF
# Use an external copy of ${bundled} to imitate a bundled one.
from ${bundled} import *
EOF
  sed -r -i "s/(install_requires=\[)/\1'${bundled}', /" setup.py
done


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files grabbit


%check
%tox


%files -n python3-grabbit -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%license LICENSE
%doc README.md
%doc examples


%changelog
%autochangelog
