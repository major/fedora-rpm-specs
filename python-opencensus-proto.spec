# Should we re-generate the Python binding code from the .proto files, instead
# of using the pre-generated code in the source tarball? Either approach is OK
# under Fedora packaging guidelines.
%bcond_with codegen

%global srcname opencensus-proto
%global _description %{expand:
Census provides a framework to define and collect stats against metrics and to
break those stats down across user-defined dimensions.

The Census framework is natively available in many languages (e.g. C++, Go, and
Java). The API interface types are defined using protos to ensure consistency
and interoperability for the different implementations.}

Name:           python-%{srcname}
Version:        0.4.1
Release:        %autorelease
Summary:        Language Independent Interface Types For OpenCensus

License:        Apache-2.0
URL:            https://github.com/census-instrumentation/%{srcname}/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
%if %{with codegen}
BuildRequires:  %{py3_dist grpcio-tools}
%endif
BuildArch:      noarch

%description %{_description}


%package -n python3-%{srcname}
Summary:        Python library generated from OpenCensus cross-language protos

%description -n python3-%{srcname} %{_description}.


%prep
%autosetup -n %{srcname}-%{version}

%if %{with codegen}
find gen-python/opencensus/proto -type f ! -name '__init__.py' -print -delete
sed -r -i 's|\bpython |%{__python3} |g' src/mkpygen.sh
%endif

sed -r -i 's/^__version__[[:blank:]]*=/# &/' gen-python/version.py
cat >> gen-python/version.py <<EOF
# Python version number is always “dev”
# https://github.com/census-instrumentation/opencensus-proto/issues/234
__version__ = '%{version}'  # Correct release version
EOF


%generate_buildrequires
cd gen-python/
%pyproject_buildrequires


%build
%if %{with codegen}
pushd src
./mkpygen.sh
popd
%endif
pushd gen-python/
%pyproject_wheel
popd


%install
pushd gen-python/
%pyproject_install
# Giving the name of the containing namespace package works acceptably.
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%pyproject_save_files opencensus
popd


%check
# Upstream has no tests.
%pyproject_check_import -e opencensus.proto.*.*.v1.* -e opencensus.proto.*.v1.*


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS CONTRIBUTING.md gen-python/README.rst

# Excluding these files makes it easier to share ownership of the namespace
# package directory, without worrying about trivial differences in the contents
# of __init__.py—which is not needed for namespace packages in recent Python
# versions anyway.
%exclude %{python3_sitelib}/opencensus/{*.py,__pycache__/}


%changelog
%autochangelog
