%global common_description %{expand:
Jedi is a static analysis tool for Python that can be used in IDEs/editors. Its
historic focus is autocompletion, but does static analysis for now as well.
Jedi is fast and is very well tested. It understands Python on a deeper level
than all other static analysis frameworks for Python.}

%if %{defined fedora}
# epel9 is missing django
%bcond_without tests
%endif

# jedi bundles 2 other projects
# when using the git tarball, the projects need to be pulled separately
# when using tarballs from PyPI, those are included
%global django_stubs_commit fd057010f6cbf176f57d1099e82be46d39b99cb9
%global typeshed_commit     ae9d4f4b21bb5e1239816c301da7b1ea904b44c3

Name:           python-jedi
Version:        0.19.2
Release:        %autorelease
Summary:        An auto completion tool for Python that can be used for text editors

# jedi is MIT
# django-stubs is MIT
# typeshed is MIT ASL 2.0
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0

URL:            https://jedi.readthedocs.org
Source0:        https://github.com/davidhalter/jedi/archive/v%{version}/jedi-%{version}.tar.gz
Source1:        https://github.com/davidhalter/django-stubs/archive/%{django_stubs_commit}/django-stubs-%{django_stubs_commit}.tar.gz
Source2:        https://github.com/davidhalter/typeshed/archive/%{typeshed_commit}/typeshed-%{typeshed_commit}.tar.gz
BuildArch:      noarch

%description %{common_description}

%package -n python3-jedi
Summary:        %{summary}
BuildRequires:  python3-devel
Provides:       bundled(python3dist(django-stubs)) = %{django_stubs_commit}
Provides:       bundled(typeshed) = %{typeshed_commit}

%description -n python3-jedi %{common_description}


%prep
%autosetup -n jedi-%{version} -p 1

# git submodules
pushd jedi/third_party
rmdir django-stubs typeshed
tar xf %{SOURCE1} && mv django-stubs-%{django_stubs_commit} django-stubs
tar xf %{SOURCE2} && mv typeshed-%{typeshed_commit} typeshed
popd
cp -p jedi/third_party/django-stubs/LICENSE.txt LICENSE-django-stubs.txt
cp -p jedi/third_party/typeshed/LICENSE LICENSE-typeshed.txt

# relax upper limits on test dependencies
sed -e 's/pytest<7.0.0/pytest/' \
    -e 's/Django<3.1/Django/' \
    -i setup.py

# Fix for compatibility with pytest 8
# Proposed upstream: https://github.com/davidhalter/jedi/pull/1996
sed -i "/def __init__/s/__init__/setUp/" test/test_utils.py

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x testing}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jedi


%check
%if %{with tests}
# %%pytest manipulates the sys.path
# test_compiled_singature
# - https://github.com/davidhalter/jedi/issues/1952
# - https://github.com/python/cpython/issues/107526
%pytest -k "\
    not test_venv_and_pths and \
    not test_compiled_signature and \
    not test_find_system_environments and \
    not test_import"
%else
%pyproject_check_import
%endif


%files -n python3-jedi -f %{pyproject_files}
%doc CHANGELOG.rst README.rst


%changelog
%autochangelog
