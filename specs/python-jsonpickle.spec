Name:           python-jsonpickle
# version is inserted into setup.cfg manually (see %%prep). Please be careful
# to use a Python-compatible version number if you need to set an "uncommon"
# version for this RPM.
Version:        4.1.2
Release:        %autorelease
Summary:        A module that allows any object to be serialized into JSON

License:        BSD-3-Clause
URL:            https://github.com/jsonpickle/jsonpickle
Source0:        %{pypi_source jsonpickle}
# Fix compatibility with pandas 3.0's new StringDtype and resolve numpy deprecation warnings
# Backport of https://github.com/jsonpickle/jsonpickle/pull/592
Patch:          fix-pandas3-stringdtype.patch

%global _docdir_fmt %{name}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
jsonpickle is a library for the two-way conversion of complex Python objects
and JSON. jsonpickle builds upon the existing JSON encoders, such as
simplejson, json, and ujson.}

%description %{_description}


%package -n python3-jsonpickle
Summary:        A module that allows any object to be serialized into JSON

%description -n python3-jsonpickle %{_description}


%prep
%autosetup -n jsonpickle-%{version} -p1

sed -r -i 's/[[:blank:]]--cov[^[:blank:]]*//g' pytest.ini

sed -i /bson/d pyproject.toml
sed -i /pymongo/d pyproject.toml
sed -i /histogram/d pyproject.toml
sed -i /black\ /d pyproject.toml
sed -i /pytest-checkdocs\ /d pyproject.toml
sed -i /pytest-cov\ /d pyproject.toml
sed -i /pytest-flake8\ /d pyproject.toml
sed -i /pytest-enabler\ /d pyproject.toml
sed -i /pytest-ruff\ /d pyproject.toml
sed -i /atheris\ /d pyproject.toml

%if 0%{?el9}
# Not yet packaged:
# [RFE:EPEL9] EPEL9 branch for python-pandas
# https://bugzilla.redhat.com/show_bug.cgi?id=2032550
# (python-scikit-learn: no EPEL9 request yet)
sed -r -i -e 's/^([[:blank:]]*)(pandas|scikit-learn)/\1# \2/' setup.cfg
%endif


%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jsonpickle


%check
# Run pytest ignoring tests that fail due to incompatible numpy/pandas versions in Rawhide
%pytest %{?el9:--ignore=jsonpickle/ext/pandas.py} --ignore=fuzzing/ -k      \
"not test_warnings and not test_ndarray_roundtrip and not test_weird_arrays \
and not test_transpose and not test_buffer and not test_as_strided          \
and not test_pre_v3_4_df_decoding"


%files -n python3-jsonpickle -f %{pyproject_files}


%changelog
%autochangelog
