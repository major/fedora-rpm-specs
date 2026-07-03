Name:           fastapi-cloud-cli
Version:        0.22.0
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
Source100:      fastapi-cloud.1
Source110:      fastapi-cloud-deploy.1
Source120:      fastapi-cloud-link.1
Source130:      fastapi-cloud-login.1
Source140:      fastapi-cloud-logs.1
Source150:      fastapi-cloud-logout.1
Source160:      fastapi-cloud-whoami.1
Source170:      fastapi-cloud-unlink.1
Source180:      fastapi-cloud-setup-ci.1
Source190:      fastapi-cloud-env.1
Source191:      fastapi-cloud-env-list.1
Source192:      fastapi-cloud-env-get.1
Source193:      fastapi-cloud-env-set.1
Source194:      fastapi-cloud-env-delete.1
Source200:      fastapi-cloud-auth.1
Source201:      fastapi-cloud-auth-login.1
Source202:      fastapi-cloud-auth-wait.1
Source210:      fastapi-cloud-apps.1
Source211:      fastapi-cloud-apps-create.1
Source212:      fastapi-cloud-apps-get.1
Source213:      fastapi-cloud-apps-link.1
Source214:      fastapi-cloud-apps-list.1
Source215:      fastapi-cloud-apps-logs.1
Source216:      fastapi-cloud-apps-unlink.1
Source217:      fastapi-cloud-apps-update.1
Source220:      fastapi-cloud-ci.1
Source221:      fastapi-cloud-ci-print-workflow.1
Source222:      fastapi-cloud-ci-setup.1
Source230:      fastapi-cloud-deployments.1
Source231:      fastapi-cloud-deployments-get.1
Source232:      fastapi-cloud-deployments-build-logs.1
Source233:      fastapi-cloud-deployments-list.1
Source240:      fastapi-cloud-teams.1
Source241:      fastapi-cloud-teams-list.1
Source242:      fastapi-cloud-teams-get.1
Source250:      fastapi-cloud-tokens.1
Source251:      fastapi-cloud-tokens-create.1
Source252:      fastapi-cloud-tokens-delete.1
Source253:      fastapi-cloud-tokens-list.1

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

# Since requirements-tests.txt contains overly-strict version bounds and
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch the requirements file. We preserve upstream’s lower bounds
# but remove upper bounds, as we must try to make do with what we have.
BuildRequires:  %{py3_dist pytest} >= 7
BuildRequires:  %{py3_dist respx} >= 0.22
BuildRequires:  %{py3_dist time-machine} >= 2.15
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


%pyproject_extras_subpkg -n fastapi-cloud-cli standard


%prep -a
# Only used for built-in update checker, which we have disabled
%pyproject_patch_dependency detect-installer:ignore


%install -a
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' \
    '%{SOURCE11}' '%{SOURCE13}' \
    '%{SOURCE100}' \
    '%{SOURCE110}' \
    '%{SOURCE120}' \
    '%{SOURCE130}' \
    '%{SOURCE140}' \
    '%{SOURCE150}' \
    '%{SOURCE160}' \
    '%{SOURCE170}' \
    '%{SOURCE180}' \
    '%{SOURCE190}' '%{SOURCE191}' '%{SOURCE192}' '%{SOURCE193}' '%{SOURCE194}' \
    '%{SOURCE200}' '%{SOURCE201}' '%{SOURCE202}' \
    '%{SOURCE210}' '%{SOURCE211}' '%{SOURCE212}' '%{SOURCE213}' '%{SOURCE214}' \
      '%{SOURCE215}' '%{SOURCE216}' '%{SOURCE217}' \
    '%{SOURCE220}' '%{SOURCE221}' '%{SOURCE222}' \
    '%{SOURCE230}' '%{SOURCE231}' '%{SOURCE232}' '%{SOURCE233}' \
    '%{SOURCE240}' '%{SOURCE241}' '%{SOURCE242}' \
    '%{SOURCE250}' '%{SOURCE251}' '%{SOURCE252}' '%{SOURCE253}'


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
