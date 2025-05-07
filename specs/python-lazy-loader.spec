%bcond tests 1

Name:           python-lazy-loader
Version:        0.4
Release:        %autorelease
Summary:        Populate library namespace without incurring immediate import costs

License:        BSD-3-Clause
URL:            https://github.com/scientific-python/lazy_loader
Source:         %{pypi_source lazy_loader}

BuildSystem:            pyproject
BuildOption(install):   -l lazy_loader

BuildArch:      noarch

%if %{with tests}
# The “test” extra includes unwanted linters, etc.; we manually BR pytest
# rather than patching out all the others from pyproject.toml.
BuildRequires:  python3dist(pytest)
# These are required for some of the tests, but are not captured in the
# metadata, so we must BR them manually as well:
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
%endif

%global common_description %{expand:
lazy-loader makes it easy to load subpackages and functions on demand.

Motivation:

• Allow subpackages to be made visible to users without incurring import costs.
• Allow external libraries to be imported only when used, improving import
  times.}

%description %{common_description}


%package -n python3-lazy-loader
Summary:        %{summary}

%description -n python3-lazy-loader %{common_description}


%check -a
%if %{with tests}
%pytest
%endif


%files -n python3-lazy-loader -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
