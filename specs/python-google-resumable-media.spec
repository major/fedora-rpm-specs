Version:        2.8.2
Name:           python-google-resumable-media
Release:        %autorelease
Summary:        Utilities for Google media downloads and resumable uploads

License:        Apache-2.0
# Since 2.8.1, https://github.com/googleapis/google-resumable-media-python has
# been archived, and the source is now managed as part of Google’s massive
# google-cloud-python monorepo, e.g.:
# https://github.com/googleapis/google-cloud-python/tree/main/packages/google-resumable-media
# The tag for a release is of the form
#   %%global tag google-resumable-media-v%%{version},
# and a GitHub archive URL would be of the form:
#   %%global forgeurl https://github.com/googleapis/google-cloud-python/
#   %%{forgeurl}/archive/%%{tag}/google-cloud-python-%%{tag}.tar.gz
# However, this archive would be 100MB+, containing many unrelated files that
# would bloat the source RPM and would need to be reviewed for any possible
# license issues. Instead, we package from the PyPI sdists, which may lack some
# useful sources (particularly, CHANGELOG.md), but which are good enough and
# are much more compact.
URL:            https://pypi.org/project/google-resumable-media
Source:         %{pypi_source google_resumable_media}

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x requests
BuildOption(install):   -l google

BuildArch:      noarch

BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist brotli}

%global _description %{expand:
%{summary}.}

%description %{_description}


%package -n python3-google-resumable-media
Summary:        %{summary}

%description -n python3-google-resumable-media %{_description}


# We don’t build a metapackage for the aiohttp extra because it currently
# requires google-auth 1.x, and Fedora has version 2.x.
#
# Please consider supporting google-auth 2.x
# https://github.com/googleapis/google-resumable-media-python/issues/417
%pyproject_extras_subpkg -n python3-google-resumable-media requests


%check -a
%pytest tests/unit


%files -n python3-google-resumable-media -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
