Name:           python-grabbit
Version:        0.2.6
Release:        %autorelease
Summary:        Get grabby with file trees

# The entire source is MIT, except:
# - The bundled grabbit/external/inflect.py is GPL-3.0-or-later, but we remove
#   it in %%prep.
# - The bundled versioneer.py (which is not packaged), and the _version.py it
#   generates (which is packaged) are CC0-1.0, which is not-allowed for code in
#   Fedora, but this case is covered by the following exception
#   (https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383):
#
#     Existing uses of CC0-1.0 on code files in Fedora packages prior to
#     2022-08-01, and subsequent upstream versions of those files in those
#     packages, continue to be allowed. We encourage Fedora package maintainers
#     to ask upstreams to relicense such files.
#   However, we patch the source to update Versioneer to version 0.29, which is
#   Unlicense (along with the _version.py it generates).
License:        MIT AND Unlicense
URL:            https://github.com/grabbles/grabbit
Source:         %{url}/archive/%{version}/grabbit-%{version}.tar.gz

# Update versioneer from 0.18 to 0.21
# Fixes Python 3.11 compatiblity (RHBZ#2026767)
# https://github.com/grabbles/grabbit/pull/93
Patch:          %{url}/pull/93.patch
# Update versioneer to 0.29
# https://github.com/grabbles/grabbit/pull/94
Patch:          %{url}/pull/94.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Grabbit is a lightweight Python package for simple queries over filenames
within a project. It is geared towards projects or applications with highly
structured filenames that allow useful queries to be performed without having
to inspect the file metadata or contents.}

%description %{_description}


%package -n python3-grabbit
Summary:        %{summary}

%description -n python3-grabbit %{_description}


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
%pyproject_save_files -l grabbit


%check
%tox


%files -n python3-grabbit -f %{pyproject_files}
%doc README.md
%doc examples/


%changelog
%autochangelog
