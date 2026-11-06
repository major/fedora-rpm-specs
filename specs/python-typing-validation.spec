Name:           python-typing-validation
Version:        2.2.1
Release:        %autorelease
Summary:        A library to perform runtime validation of Python objects using type hints

License:        LGPL-3.0-or-later
URL:            https://github.com/hashberg-io/typing-validation
Source:         https://github.com/hashberg-io/typing-validation/archive/v%{version}/typing-validation-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install):  --assert-license typing_validation

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli
#tests
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest

%global _description %{expand:
A library to perform runtime validation of Python objects using type hints.}

%description %_description

%package -n     python3-typing-validation
Summary:        %{summary}

%description -n python3-typing-validation %_description

%prep -a
%pyproject_patch_dependency hatchling:drop_upper
# Warnings-as-errors makes sense for upstream CI, but is too brittle for packaging
tomcli set pyproject.toml lists delitem tool.pytest.ini_options.filterwarnings error

%check -a
# test_every_form_is_accepted_and_inferred invokes mypy, which exposes upstream types incompatibilities
# test_typing_dot_typeform_has_not_landed_yet is intentionally expected to fail once Python 3.15 provides typing.TypeForm; Fedora builds with Python 3.15.
%pytest -k 'not test_every_form_is_accepted_and_inferred and not test_typing_dot_typeform_has_not_landed_yet'


%files -n python3-typing-validation -f %{pyproject_files}

%changelog
%autochangelog
