%global forgeurl https://github.com/fsspec/universal_pathlib

%global _description %{expand:
Universal Pathlib is a Python library that extends the pathlib.Path API to
support a variety of backend filesystems via filesystem_spec.}

Name:           python-universal-pathlib
Version:        0.2.5
Release:        %{autorelease}
Summary:        Pathlib api extended to use fsspec backends

# The entire source is MIT, except that upath/_compat.py contains code from
# CPython (see https://github.com/python/cpython/blob/v3.12.2/Lib/pathlib.py),
# which is Python-2.0.1.
License:        MIT AND Python-2.0.1
URL:            %forgeurl

%forgemeta
Source:         %forgesource
BuildArch:      noarch

%description %_description

%package -n python3-universal-pathlib
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

# Parts of upath/_compat.py are copied from CPython 3.12. Since the relevant
# work began on 2024-02-20 in
# https://github.com/fsspec/universal_pathlib/pull/200 and was merged in
# https://github.com/fsspec/universal_pathlib/pull/200 on 2024-03-03, we
# ascribe the code to the latest 3.12 release at the time.
Provides:       bundled(python3-libs) = 3.12.2


%description -n python3-universal-pathlib %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%forgeautosetup

# remove linters etc. from deps
echo "Removing linters etc. from build deps"
sed -i \
    -e '/"pytest-cov.*"/d' \
    -e '/"pylint.*"/d' \
    -e '/"mypy.*"/d' \
    -e '/"pytest-mypy-plugins.*"/d' \
    -e '/"pytest-sugar.*"/d' \
    pyproject.toml

deps_to_remove=("s3fs" "adlfs" "moto\[s3,server\]")
echo "Removing deps that are unavailable in Fedora: ${deps_to_remove[*]}"
(IFS="|" ; sed -Ei "/(${deps_to_remove[*]})/d" pyproject.toml)

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x dev -x tests


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l upath

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
web_tests_to_ignore="${web_tests_to_ignore-} --ignore=upath/tests/implementations/test_http.py"
web_tests_to_ignore="${web_tests_to_ignore-} --ignore=upath/tests/implementations/test_github.py"
%pytest ${web_tests_to_ignore-}
# check imports instead
%pyproject_check_import

# LICENSE/COPYING are included in the dist-info, so we do not need to
# explicitly list them again
%files -n python3-universal-pathlib -f %{pyproject_files}
%doc README.md CHANGELOG.md

%files doc
%doc notebooks
%license LICENSE

%changelog
%autochangelog
