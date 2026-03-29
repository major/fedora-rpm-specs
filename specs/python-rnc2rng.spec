Name:           python-rnc2rng
Version:        2.7.0
Release:        %autorelease
Summary:        RELAX NG Compact to regular syntax conversion library

# The entire package is MIT, except that rnc2rng/serialize.py is
# LicenseRef-Fedora-Public-Domain:
#   “This file released to the Public Domain by David Mertz”
#   https://gitlab.com/fedora/legal/fedora-license-data/-/work_items/728
#   https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/838
License:        MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/djc/rnc2rng
Source0:        %{pypi_source rnc2rng}
# Man page hand-written for Fedora in groff_man(7) syntax, based on the
# contents of README.rst and rnc2rng/__main__.py.
Source1:        rnc2rng.1

# Remove useless shebangs, execute bits
# https://github.com/djc/rnc2rng/pull/54
Patch:          %{url}/pull/54.patch

BuildSystem:    pyproject
BuildOption(install):   -l rnc2rng

BuildArch:      noarch

%global common_description %{expand:
Converts RELAX NG schemata in Compact syntax (rnc) to the equivalent schema in
the XML-based default RELAX NG syntax.}

%description %{common_description}


%package -n python3-rnc2rng
Summary:        %{summary}

%description -n python3-rnc2rng %{common_description}


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check -a
%{py3_test_envvars} %{python3} test.py


%files -n python3-rnc2rng -f %{pyproject_files}
%doc AUTHORS
%doc README.rst

%{_bindir}/rnc2rng
%{_mandir}/man1/rnc2rng.1*


%changelog
%autochangelog
