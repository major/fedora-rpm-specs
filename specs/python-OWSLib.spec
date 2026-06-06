Name:           python-OWSLib
Version:        0.36.0
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

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --extras test
BuildOption(install): --assert-license owslib

BuildArch:      noarch

BuildRequires:  tomcli

# Additional test dependencies from the “dev” extra, which also contains
# unwanted linting/coverage dependencies and other unnecessary dependencies.
BuildRequires:  %{py3_dist pytest_httpserver}
BuildRequires:  %{py3_dist Pillow}

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
# after Fedora 44.
Obsoletes:      python-OWSLIB-doc < 0.32.0-1

%description -n python3-OWSLib %{common_description}


%prep -a
# Don’t analyze/report test coverage
tomcli set pyproject.toml lists delitem tool.pytest.addopts -- '--cov\b.*'
# We cannot possibly respect an upper bound on the version of setuptools!
# According to https://github.com/geopython/OWSLib/pull/1031, upstream pinned
# this “for Ubuntu 24.04 compatibility,” whatever that means.
%pyproject_patch_dependency setuptools:drop_upper


%check -a
# Otherwise, pytest finds the package twice in the Python path and complains.
rm --recursive owslib

# These require test data files from tests/resources/, which we have removed:
ignore="${ignore-} --ignore-glob=tests/doctests/*.txt"
ignore="${ignore-} --ignore-glob=tests/test_wps_request*.py"
ignore="${ignore-} --ignore-glob=tests/test_wps_response*.py"
ignore="${ignore-} --ignore=tests/test_iso_parsing.py"
ignore="${ignore-} --ignore=tests/test_ows_interfaces.py"
ignore="${ignore-} --ignore=tests/test_owscontext_atomxml.py"
ignore="${ignore-} --ignore=tests/test_remote_metadata.py"
ignore="${ignore-} --ignore=tests/test_wfs_generic.py"
ignore="${ignore-} --ignore=tests/test_wms_datageo_130.py"
ignore="${ignore-} --ignore=tests/test_wms_jpl_capabilities.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_bbox.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_ceda.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_emu_all.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_usgs.py"
ignore="${ignore-} --ignore=tests/test_wps_execute.py"
ignore="${ignore-} --ignore=tests/test_wps_execute_invalid_request.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_52n.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_ceda.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_usgs.py"
k="${k-}${k+ and }not TestOffline"
k="${k-}${k+ and }not test_aus"
k="${k-}${k+ and }not test_decode_full_json"
k="${k-}${k+ and }not test_decode_single_json"
k="${k-}${k+ and }not test_distributor"
k="${k-}${k+ and }not test_dq_dataquality"
k="${k-}${k+ and }not test_get_all_contacts"
k="${k-}${k+ and }not test_gm03"
k="${k-}${k+ and }not test_identification"
k="${k-}${k+ and }not test_identification_contact"
k="${k-}${k+ and }not test_identification_date"
k="${k-}${k+ and }not test_identification_extent"
k="${k-}${k+ and }not test_identification_keywords"
k="${k-}${k+ and }not test_load_bulk"
k="${k-}${k+ and }not test_load_parse"
k="${k-}${k+ and }not test_md_distribution"
k="${k-}${k+ and }not test_md_featurecataloguedesc"
k="${k-}${k+ and }not test_md_imagedescription"
k="${k-}${k+ and }not test_md_parsing"
k="${k-}${k+ and }not test_md_reference_system"
k="${k-}${k+ and }not test_metadata"
k="${k-}${k+ and }not test_online_distribution"
k="${k-}${k+ and }not test_responsibility"
k="${k-}${k+ and }not test_service"
k="${k-}${k+ and }not test_service2"
k="${k-}${k+ and }not test_spatial_parsing"
k="${k-}${k+ and }not test_wps_checkStatus"
k="${k-}${k+ and }not test_wps_getOperationByName"
k="${k-}${k+ and }not test_wps_literal_data_input_parsing_references"
k="${k-}${k+ and }not test_wps_process_properties"
k="${k-}${k+ and }not test_wps_process_representation"
k="${k-}${k+ and }not test_wps_response_with_lineage"

%pytest -m 'not online' -k "${k-}" ${ignore-} --verbose -rs


%files -n python3-OWSLib -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
