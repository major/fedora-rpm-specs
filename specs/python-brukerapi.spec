Name:           python-brukerapi
Version:        0.2.2
Release:        %autorelease
Summary:        Python package providing I/O interface for Bruker data sets

# SPDX
License:        MIT
URL:            https://github.com/isi-nmr/brukerapi-python
Source0:        %{url}/archive/v%{version}/brukerapi-python-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
# output; see:
#
# Interest in man pages?
# https://github.com/isi-nmr/brukerapi-python/issues/19
Source10:       bruker.1
Source11:       bruker-filter.1
Source12:       bruker-report.1
Source13:       bruker-split.1

BuildSystem:            pyproject
BuildOption(install):   -l brukerapi

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
A Python package providing I/O interface for Bruker data sets.}

%description %{common_description}


%package -n python3-brukerapi
Summary:        %{summary}

Obsoletes:      python-brukerapi-doc < 0.1.10-1

%description -n python3-brukerapi %{common_description}


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'


%check -a
# We avoid tests requiring data from zenodo,
# https://doi.org/10.5281/zenodo.4522220. Not only do we not want to consider
# the licenses of these data files, but they are also uncomfortably large, 2.2
# GB, and we don’t want to burden mirrors and users with such an enormous
# source RPM. Trick the code in conftest.py into not trying to download these
# data files.
mkdir test/zenodo_zips
for zip in '0.2H2.zip' \
    '20200612_094625_lego_phantom_3_1_2.zip' \
    '20210128_122257_LEGO_PHANTOM_API_TEST_1_1.zip'
do
    # Make an empty zip file so the test code doesn’t try to re-download
    %{python3} -m zipfile -c "test/zenodo_zips/${zip}"
done

# Avoid tests that try to use any external data sets
ignore="${ignore-} --ignore=test/test_split.py"
ignore="${ignore-} --ignore=test/test_jcampdx.py"
ignore="${ignore-} --ignore=test/test_random_access.py"
ignore="${ignore-} --ignore=test/test_dataset.py"

# We are not left with a great many tests, but we run what we can.
%pytest -v ${ignore-}


%files -n python3-brukerapi -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst
%doc examples/

%{_bindir}/bruker
%{_mandir}/man1/bruker*.1*


%changelog
%autochangelog
