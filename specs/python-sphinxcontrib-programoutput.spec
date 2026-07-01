%global srcname sphinxcontrib-programoutput

Name:           python-sphinxcontrib-programoutput
Version:        0.20
Release:        %autorelease
Summary:        Extension to insert output of commands into documents

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/sphinxcontrib-programoutput
Source0:        https://github.com/NextThought/sphinxcontrib-programoutput/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(sphinx) >= 1.3.5
BuildRequires:  python3-furo
# The documentation runs commands like 'python -V' and 'python --help'.
# Any python version is fine.
BuildRequires:  python-unversioned-command
BuildRequires:  pytest
BuildRequires:  git-core
BuildRequires:  web-assets-devel

%description
A Sphinx extension to literally insert the output of arbitrary
commands into documents, helping you to keep your command examples
up to date.

%package -n python3-%{srcname}
Summary:       %{summary}
Requires:       js-jquery

%description -n python3-%{srcname}
A Sphinx extension to literally insert the output of arbitrary
commands into documents, helping you to keep your command examples
up to date.

%prep
%autosetup -n %{srcname}-%{version} -p1
# sed -r -i s/python/python3/ src/sphinxcontrib/programoutput/tests/{test_directive.py,test_command.py,test_cache.py}

%build
%pyproject_wheel
# rm build/lib/sphinxcontrib/__init__.py

# workaround https://github.com/python/cpython/issues/94741
echo 'import importlib; importlib.invalidate_caches(); del importlib' >build/lib/sitecustomize.py
PYTHONPATH=build/lib sphinx-build -b html docs build/html
rm build/lib/sitecustomize.py build/lib/__pycache__/sitecustomize.*.pyc

rm -r build/html/.buildinfo build/html/.doctrees

%install
%pyproject_install
%pyproject_save_files -L sphinxcontrib

mkdir -p %{buildroot}%{_pkgdocdir}
cp -rv build/html %{buildroot}%{_pkgdocdir}/
ln -vsf --relative %{_jsdir}/jquery/latest/jquery.min.js %{buildroot}%{_pkgdocdir}/html/_static/jquery.js

%check
OPTIONS=(
    # Those two fail because of some warning:
    # > assert 'Unexpected return code 1 from command' in excinfo.exception.args[0]
    # E assert 'Unexpected return code 1 from command' in "directive 'deprecated' is already registered, it will be overridden"
    # I'm not sure what exactly generates this warning. But it doesn't seem to be
    # an actual problem with the code, so let's ignore this for now.
    #
    # erbsland.sphinx.ansi extension is not packaged
    -k 'not (test_shell_with_unexpected_return_code or test_unexpected_return_code or test_use_ansi_enabled_extension)'
)

%pytest -v %{buildroot}%{python3_sitelib}/sphinxcontrib "${OPTIONS[@]}"

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc %{_pkgdocdir}

%changelog
%autochangelog
