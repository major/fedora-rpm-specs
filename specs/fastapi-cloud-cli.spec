Name:           fastapi-cloud-cli
Version:        0.14.0
Release:        %autorelease
Summary:        Deploy and manage FastAPI Cloud apps from the command line

License:        MIT
URL:            https://github.com/fastapilabs/fastapi-cloud-cli
# The GitHub archive contains a few useful files that the PyPI sdist does not,
# such as the release notes.
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Written for Fedora in groff_man(7) format based on --help output
Source100:      fastapi-cloud.1
Source110:      fastapi-cloud-deploy.1
Source120:      fastapi-cloud-link.1
Source130:      fastapi-cloud-login.1
Source140:      fastapi-cloud-logs.1
Source150:      fastapi-cloud-logout.1
Source160:      fastapi-cloud-whoami.1
Source170:      fastapi-cloud-unlink.1
Source180:      fastapi-cloud-env.1
Source181:      fastapi-cloud-env-list.1
Source182:      fastapi-cloud-env-set.1
Source183:      fastapi-cloud-env-delete.1

# Downstream-only; patch out coverage from script test
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-coverage-from-script-test.patch

BuildSystem:            pyproject
BuildOption(install):   -L fastapi_cloud_cli
BuildOption(generate_buildrequires): -x standard

BuildArch:      noarch

%py_provides python3-fastapi-cloud-cli

# Since requirements-tests.txt contains overly-strict version bounds and
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch the requirements file. We preserve upstream’s lower bounds
# but remove upper bounds, as we must try to make do with what we have.
BuildRequires:  %{py3_dist pytest} >= 7
BuildRequires:  %{py3_dist respx} >= 0.22
BuildRequires:  %{py3_dist time-machine} >= 2.15

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%pyproject_extras_subpkg -n fastapi-cloud-cli standard


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' '%{SOURCE110}' '%{SOURCE120}' '%{SOURCE130}' \
    '%{SOURCE140}' '%{SOURCE150}' '%{SOURCE160}' '%{SOURCE170}' \
    '%{SOURCE180}' '%{SOURCE181}' '%{SOURCE182}' '%{SOURCE183}'


%check -a
%pytest -v


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc release-notes.md

# This package does not provide its own executable entry point; instead, it
# adds a “fastapi cloud” command to the fastapi CLI (entry point in
# python3-fastapi; separate package fastapi-cli also relevant). These man pages
# integrate with those in python3-fastapi.
%{_mandir}/man1/fastapi-cloud.1*
%{_mandir}/man1/fastapi-cloud-*.1*


%changelog
%autochangelog
