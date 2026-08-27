Name:           python-bidict
Version:        0.24.1
Release:        %autorelease
Summary:        Bidirectional mapping library for Python

License:        MPL-2.0
URL:            https://bidict.readthedocs.io
%global forgeurl https://github.com/jab/bidict
Source:         %{forgeurl}/archive/v%{version}/bidict-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --dependency-groups test
BuildOption(install): --assert-license bidict

BuildArch:      noarch

%global common_description %{expand:
The bidirectional mapping library for Python.}

%description %{common_description}


%package -n     python3-bidict
Summary:        %{summary}

%description -n python3-bidict %{common_description}


%prep -a
# We must work with what we have, and compatibility is good in practice.
%pyproject_patch_dependency uv_build:drop_upper

# We have no use for benchmarking
%pyproject_patch_dependency pytest-benchmark:ignore
# Not packaged; potentially useful, but we can get by without it
%pyproject_patch_dependency pytest-sphinx:ignore
# Not packaged; used for only one doctest, which we ignore
%pyproject_patch_dependency sortedcollections:ignore
# Mentioned in documentation, but doesn’t appear in an actual doctest
%pyproject_patch_dependency sortedcontainers:ignore
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency coverage:ignore
%pyproject_patch_dependency ty:ignore


%check -a
# This contains one doctest, which requires the sortedcollections dependency.
# It’s not worth maintaining the dependency solely for that, especially as it
# is otherwise not needed in Fedora at all.
ignore="${ignore-} --ignore=docs/extending.rst"

%pytest ${ignore-} -k "${k-}"


%files -n python3-bidict -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
