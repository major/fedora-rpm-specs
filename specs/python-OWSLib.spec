Name:           python-OWSLib
Version:        0.35.0
Release:        %autorelease
Summary:        OGC Web Service utility library

License:        BSD-3-Clause
URL:            https://geopython.github.io/OWSLib
# A filtered source archive, obtained by (see Source1):
#
#   ./get_source %%{version}
#
# is required because tests/resources/ contains XML data files that appear to
# have been pulled from various GIS databases, and the license terms for these
# files are unclear.
#
# The unfiltered base source URL would be:
#
# https://github.com/geopython/OWSLib/archive/%%{version}/OWSLib-%%{version}.tar.gz
#
# We *could* use the PyPI sdist, which does not contain tests/resources/, but
# it also does not contain any tests at all. We can still run some tests
# without the XML files, and we would like to do so.
Source0:        OWSLib-%{version}-filtered.tar.zst
Source1:        get_source

BuildSystem:            pyproject
BuildOption(install):   -l owslib

BuildArch:      noarch

# Tests; dependencies are in requirements-dev.txt.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest_httpserver}
BuildRequires:  %{py3_dist Pillow}
# We don’t have pytest-socket packaged, and we can get by without it.
# - pytest-socket
# We don’t use tox to run the tests. It would run "python3 setup.py develop",
# which is unwanted.
# - tox
# Unwanted linting/coverage dependencies:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# - coverage
# - coveralls
# - flake8
# - pytest-cov
# These are just for the maintainer to upload to PyPI.
# - build
# - twine

%global common_description %{expand:
OWSLib is a Python package for client programming with Open Geospatial
Consortium (OGC) web service (hence OWS) interface standards, and their related
content models.

Full documentation is available at http://geopython.github.io/OWSLib

OWSLib provides a common API for accessing service metadata and wrappers for
numerous OGC Web Service interfaces.}

%description %{common_description}


%package -n python3-OWSLib
Summary:        %{summary}

%py_provides python3-owslib

# The -doc subpackage was removed for Fedora 42; we can remove this Obsoletes
# after Fedora 44. (EPEL10 never had a -doc subpackage.)
Obsoletes:      python-OWSLIB-doc < 0.32.0-1

%description -n python3-OWSLib %{common_description}


%prep -a
# Don’t analyze/report test coverage
sed -r -i 's/^([[:blank:]]*)(--cov\b)/\1# \2/' tox.ini


%check -a
# Otherwise, pytest finds the package twice in the Python path and complains.
rm -rf owslib

# These require test data files from tests/resources/, which we have removed:
ignore="${ignore-} --ignore-glob=tests/doctests/*.txt"
k="${k-}${k+ and }not test_gm03"
ignore="${ignore-} --ignore=tests/test_iso_parsing.py"
ignore="${ignore-} --ignore=tests/test_ows_interfaces.py"
ignore="${ignore-} --ignore=tests/test_owscontext_atomxml.py"
k="${k-}${k+ and }not test_decode_single_json"
k="${k-}${k+ and }not test_load_parse"
k="${k-}${k+ and }not test_decode_full_json"
k="${k-}${k+ and }not test_load_bulk"
ignore="${ignore-} --ignore=tests/test_remote_metadata.py"
k="${k-}${k+ and }not TestOffline"
ignore="${ignore-} --ignore=tests/test_wfs_generic.py"
ignore="${ignore-} --ignore=tests/test_wms_datageo_130.py"
ignore="${ignore-} --ignore=tests/test_wms_jpl_capabilities.py"
k="${k-}${k+ and }not test_wps_getOperationByName"
k="${k-}${k+ and }not test_wps_checkStatus"
k="${k-}${k+ and }not test_wps_process_representation"
k="${k-}${k+ and }not test_wps_process_properties"
k="${k-}${k+ and }not test_wps_literal_data_input_parsing_references"
k="${k-}${k+ and }not test_wps_response_with_lineage"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_bbox.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_ceda.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_emu_all.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_usgs.py"
ignore="${ignore-} --ignore=tests/test_wps_execute.py"
ignore="${ignore-} --ignore=tests/test_wps_execute_invalid_request.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_52n.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_ceda.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_usgs.py"
ignore="${ignore-} --ignore-glob=tests/test_wps_request*.py"
ignore="${ignore-} --ignore-glob=tests/test_wps_response*.py"
k="${k-}${k+ and }not test_metadata"
k="${k-}${k+ and }not test_responsibility"
k="${k-}${k+ and }not test_distributor"
k="${k-}${k+ and }not test_online_distribution"
k="${k-}${k+ and }not test_identification"
k="${k-}${k+ and }not test_identification_contact"
k="${k-}${k+ and }not test_identification_date"
k="${k-}${k+ and }not test_identification_extent"
k="${k-}${k+ and }not test_identification_keywords"
k="${k-}${k+ and }not test_get_all_contacts"
k="${k-}${k+ and }not test_aus"
k="${k-}${k+ and }not test_service"
k="${k-}${k+ and }not test_md_featurecataloguedesc"
k="${k-}${k+ and }not test_md_imagedescription"
k="${k-}${k+ and }not test_dq_dataquality"
k="${k-}${k+ and }not test_md_reference_system"
k="${k-}${k+ and }not test_service2"
k="${k-}${k+ and }not test_md_distribution"

%pytest -m 'not online' -k "${k-}" ${ignore-} -v -rs


%files -n python3-OWSLib -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
