Name:           python-gcsfs
Version:        2025.7.0
Release:        %autorelease
Summary:        Convenient Filesystem interface over GCS

# The entire source is BSD-3-Clause, except for versioneer.py and the
# _version.py file it generates, which are both Unlicense.
License:        BSD-3-Clause AND Unlicense
URL:            https://github.com/fsspec/gcsfs
# We must use the GitHub archive rather than the PyPI sdist if we want to have
# all the necessary files to build the Sphinx docs.
Source:         %{url}/archive/%{version}/gcsfs-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l gcsfs
BuildOption(generate_buildrequires): -x gcsfuse,crc
# gcsfs.cli.gcsfuse imports click (which is not otherwise required) and also
# tries to import a nonexistent 'gcsfs.gcsfuse' module; this seems like a bug
BuildOption(check):     -e 'gcsfs.cli.gcsfuse'

BuildArch:      noarch

# Test dependencies; see environment_gcsfs.yaml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-timeout}

# Dropped for F43; remove Obsoletes after F45.
Obsoletes:      python-gcsfs-doc < 2025.5.1-2

%global common_description %{expand:
Pythonic file-system interface for Google Cloud Storage.}

%description %{common_description}


%package -n     python3-gcsfs
Summary:        %{summary}

%description -n python3-gcsfs %{common_description}


%pyproject_extras_subpkg -n python3-gcsfs gcsfuse crc


%prep -a
# Do not pin the exact corresponding version of fsspec; this makes sense on
# PyPI since both are developed under the same organization and have
# coordinated releases, but it’s unlikely we’ll be able to maintain this level
# of coordination downstream, and it’s better to have “possible” breakage from
# version skew than *guaranteed* breakage from version skew.
sed -r -i 's/==.*//' requirements.txt


%check -a
# These tests would require docker (and probably network access).
ignore="${ignore-} --ignore=gcsfs/tests/derived/gcsfs_test.py"
ignore="${ignore-} --ignore=gcsfs/tests/test_core.py"
ignore="${ignore-} --ignore=gcsfs/tests/test_inventory_report_listing.py"
k="${k-}${k+ and }not test_metadata_read_permissions"
k="${k-}${k+ and }not test_map_"
k="${k-}${k+ and }not test_new_bucket"

# These tests would require network access and/or cloud resources.
k="${k-}${k+ and }not test_credentials_from_raw_token"

%pytest ${ignore-} -k "${k-}" -v


%files -n python3-gcsfs -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
