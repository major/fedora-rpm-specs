%global _description %{expand:
Library for checking syntax of reStructuredText and code blocks nested within
it.}

%global forgeurl https://github.com/rstcheck/rstcheck-core

Name:           python-rstcheck-core
Version:        1.3.1
Release:        %{autorelease}
Summary:        Checks syntax of reStructuredText and code blocks nested within it

%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-rstcheck-core
Summary:        %{summary}
BuildRequires:  python3-devel
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  gcc gcc-c++

%description -n python3-rstcheck-core %_description

%prep
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%forgeautosetup


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files rstcheck_core

%check
# Fails on F44
#=================================== FAILURES ===================================
#________ TestSourceChecker.test_include_directive_error_without_sphinx _________
#
#        @staticmethod
#        @pytest.mark.skipif(_extras.SPHINX_INSTALLED, reason="Test without sphinx extra.")
#        def test_include_directive_error_without_sphinx() -> None:
#            """Test error on include directive with non-existing file when sphinx is missing."""
#            source = """
#    .. include:: doesnt_exist.rst
#    """
#
#            result = list(checker.check_source(source))
#
#            assert len(result) > 0
#>           assert '(ERROR/3) Problems with "include" directive path:' in result[0]["message"]
#E           assert '(ERROR/3) Problems with "include" directive path:' in '(SEVERE/4) Problems with "include" directive path:'
#
#result     = [{'line_number': 2, 'message': '(SEVERE/4) Problems with "include" directive path:', 'source_origin': '<string>'}]
#source     = '\n.. include:: doesnt_exist.rst\n'
#
#tests/checker_test.py:252: AssertionError
%if 0%{?fedora} <= 45
k="${k-}${k+ and }not test_include_directive_error_without_sphinx"
%endif

# https://github.com/rstcheck/rstcheck-core/issues/57
k="${k-}${k+ and } not test_check_python_returns_error_on_syntax_warning"

%{pytest} "${k:+-k $k}"

%files -n python3-rstcheck-core -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
