Name:           fastapi-cloud-cli
Version:        0.25.0
Release:        %autorelease
Summary:        Deploy and manage FastAPI Cloud apps from the command line

License:        MIT
URL:            https://github.com/fastapilabs/fastapi-cloud-cli
# The GitHub archive contains a few useful files that the PyPI sdist does not,
# such as the release notes.
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Written for Fedora in groff_man(7) format based on --help output
Source11:       fastapi-deploy.1
Source13:       fastapi-login.1
Source1000:      fastapi-cloud.1
Source1100:      fastapi-cloud-deploy.1
Source1200:      fastapi-cloud-link.1
Source1300:      fastapi-cloud-login.1
Source1400:      fastapi-cloud-logs.1
Source1500:      fastapi-cloud-logout.1
Source1600:      fastapi-cloud-whoami.1
Source1700:      fastapi-cloud-unlink.1
Source1800:      fastapi-cloud-setup-ci.1
Source1900:      fastapi-cloud-env.1
Source1910:      fastapi-cloud-env-list.1
Source1920:      fastapi-cloud-env-get.1
Source1930:      fastapi-cloud-env-set.1
Source1940:      fastapi-cloud-env-delete.1
Source2000:      fastapi-cloud-auth.1
Source2010:      fastapi-cloud-auth-login.1
Source2020:      fastapi-cloud-auth-wait.1
Source2100:      fastapi-cloud-apps.1
Source2110:      fastapi-cloud-apps-create.1
Source2120:      fastapi-cloud-apps-get.1
Source2130:      fastapi-cloud-apps-link.1
Source2140:      fastapi-cloud-apps-list.1
Source2150:      fastapi-cloud-apps-logs.1
Source2160:      fastapi-cloud-apps-unlink.1
Source2170:      fastapi-cloud-apps-update.1
Source2200:      fastapi-cloud-ci.1
Source2210:      fastapi-cloud-ci-print-workflow.1
Source2220:      fastapi-cloud-ci-setup.1
Source2300:      fastapi-cloud-deployments.1
Source2310:      fastapi-cloud-deployments-get.1
Source2320:      fastapi-cloud-deployments-build-logs.1
Source2330:      fastapi-cloud-deployments-list.1
Source2400:      fastapi-cloud-domains.1
Source2410:      fastapi-cloud-domains-add.1
Source2420:      fastapi-cloud-domains-get.1
Source2430:      fastapi-cloud-domains-list.1
Source2440:      fastapi-cloud-domains-remove.1
Source2450:      fastapi-cloud-domains-restart.1
Source2500:      fastapi-cloud-integrations.1
Source2510:      fastapi-cloud-integrations-providers.1
Source2511:      fastapi-cloud-integrations-providers-list.1
Source2520:      fastapi-cloud-integrations-resources.1
Source2521:      fastapi-cloud-integrations-resources-connect.1
Source2522:      fastapi-cloud-integrations-resources-disconnect.1
Source2523:      fastapi-cloud-integrations-resources-get.1
Source2524:      fastapi-cloud-integrations-resources-list.1
Source2600:      fastapi-cloud-teams.1
Source2610:      fastapi-cloud-teams-list.1
Source2620:      fastapi-cloud-teams-get.1
Source2700:      fastapi-cloud-tokens.1
Source2710:      fastapi-cloud-tokens-create.1
Source2720:      fastapi-cloud-tokens-delete.1
Source2730:      fastapi-cloud-tokens-list.1

# Downstream-only; patch out coverage from script test
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-coverage-from-script-test.patch

# Downstream-only: disable built-in update checker
#
# Informing the user about available upstream updates does not make sense for a
# distribution package.
#
# Move the detect_installer import to the function where it is used so we
# can omit the dependency.
Patch:          0002-Downstream-only-disable-built-in-update-checker.patch

BuildSystem:    pyproject
BuildOption(install): --no-assert-license fastapi_cloud_cli
BuildOption(generate_buildrequires): --extras standard

BuildArch:      noarch

%py_provides python3-fastapi-cloud-cli

# Since the “dev” dependency group contains overly-strict version bounds and
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch the requirements file.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist respx}
BuildRequires:  %{py3_dist time-machine}
BuildRequires:  %{py3_dist inline-snapshot}
# The “fastapi cloud setup-ci” command uses gh (the GitHub CLI) when available,
# falling back to git (git-core suffices) where it can. One of these is
# required both for testing the command and for using it at runtime.
#
# With gh, according to the source code:
#   - getting the remote origin URL respects “gh repo set-default”
#   - getting the default branch is possible
#   - GitHub secrets can be set (otherwise they would have to be set manually)
# Since gh gives more complete functionality, we choose to depend on it
# unconditionally. This could be (at runtime) a weak dependency, but if someone
# is trying to minimize a FastAPI installation, then they will probably try to
# take measures to avoid pulling in fastapi-cloud-cli altogether. We therefore
# make it a hard dependency, erring on the side of delivering full
# functionality.
BuildRequires:  gh
Requires:       gh

# fastapi-deploy and fastapi-login man page moved from here:
Conflicts:      python3-fastapi < 0.136.3-3

%description
%{summary}.


%pyproject_extras_subpkg --name fastapi-cloud-cli standard


%prep -a
# Only used for built-in update checker, which we have disabled
%pyproject_patch_dependency detect-installer:ignore


%install -a
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' \
    '%{SOURCE11}' '%{SOURCE13}' \
    '%{SOURCE1000}' \
    '%{SOURCE1100}' \
    '%{SOURCE1200}' \
    '%{SOURCE1300}' \
    '%{SOURCE1400}' \
    '%{SOURCE1500}' \
    '%{SOURCE1600}' \
    '%{SOURCE1700}' \
    '%{SOURCE1800}' \
    '%{SOURCE1900}' '%{SOURCE1910}' '%{SOURCE1920}' '%{SOURCE1930}' \
      '%{SOURCE1940}' \
    '%{SOURCE2000}' '%{SOURCE2010}' '%{SOURCE2020}' \
    '%{SOURCE2100}' '%{SOURCE2110}' '%{SOURCE2120}' '%{SOURCE2130}' \
      '%{SOURCE2140}' '%{SOURCE2150}' '%{SOURCE2160}' '%{SOURCE2170}' \
    '%{SOURCE2200}' '%{SOURCE2210}' '%{SOURCE2220}' \
    '%{SOURCE2300}' '%{SOURCE2310}' '%{SOURCE2320}' '%{SOURCE2330}' \
    '%{SOURCE2400}' '%{SOURCE2410}' '%{SOURCE2420}' '%{SOURCE2430}' \
      '%{SOURCE2440}' '%{SOURCE2450}' \
    '%{SOURCE2500}' '%{SOURCE2510}' '%{SOURCE2511}' '%{SOURCE2520}' \
      '%{SOURCE2521}' '%{SOURCE2522}' '%{SOURCE2523}' '%{SOURCE2524}' \
    '%{SOURCE2600}' '%{SOURCE2610}' '%{SOURCE2620}' \
    '%{SOURCE2700}' '%{SOURCE2710}' '%{SOURCE2720}' '%{SOURCE2730}'


%check -a
# We have disabled the built-in update checker.
k="${k-}${k+ and }not test_embedded_fastapi_cli_prints_forced_update_message"
skips="${skips-} --ignore=tests/test_version_check.py"

%pytest ${skips-} -k "${k-}" --verbose


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
%{_mandir}/man1/fastapi-deploy.1*
%{_mandir}/man1/fastapi-login.1*


%changelog
%autochangelog
