Name:           python-PyLink
Version:        0.3.2
Release:        %autorelease
Summary:        Universal communication interface using File-Like API

License:        BSD-3-Clause
URL:            https://github.com/SalemHarrache/PyLink
Source:         %{pypi_source PyLink}

BuildSystem:            pyproject
BuildOption(install):   -l pylink
BuildOption(check):     -e pylink.test_links

BuildArch:      noarch

%global common_description %{expand:
Pylink offers a universal communication interface using File-Like API. For now,
only the TCP, UDP, Serial and GSM interfaces are supported.

The aim of this project is to allow any type of communication. It is best
suited for projects that have various ways of communicating including IP
remote or local serial communication.}

%description %{common_description}


%package -n python3-pylink
Summary:        %{summary}

# Renamed binary package from python3-PyLink to python3-pylink to match the
# canonical name; since this happened during development of Fedora 43, we can
# remove the upgrade path after Fedora 45.
Obsoletes:      python3-PyLink < 0.3.2-34
%py_provides    python3-PyLink

%description -n python3-pylink %{common_description}


# We cannot run tests because they all require network access.


%files -n python3-pylink -f %{pyproject_files}
%license LICENSE
%doc AUTHORS CHANGES.rst README.rst


%changelog
%autochangelog
