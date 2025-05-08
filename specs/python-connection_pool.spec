Name:           python-connection_pool
Version:        0.0.3
Release:        %autorelease
Summary:        Thread-safe connection pool for python

# SPDX
License:        MIT
URL:            https://github.com/zhouyl/ConnectionPool
Source:         %{url}/archive/%{version}/connection_pool-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l connection_pool

BuildArch:      noarch

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-connection-pool
Summary:        %{summary}

# The source package is named python-connection_pool for historical reasons.
# The binary package, python3-connection-pool, is named using the canonical
# project name[1]; see also [2].
#
# The %%py_provides macro is used to provide an upgrade path from
# python3-connection_pool and to produce the appropriate Provides for the
# importable module[3].
#
# [1] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_canonical_project_name
# [2] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# [3] https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules

# Provide an upgrade path; we can remove this after Fedora 45.
%py_provides python3-connection_pool
Obsoletes:      python3-connection_pool < 0.0.3-18

%description -n python3-connection-pool %{common_description}


# Upstream provides no tests.


%files -n python3-connection-pool -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
