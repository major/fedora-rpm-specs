%bcond tests 1

Version:        2.7.0
Name:           python-google-resumable-media
Release:        %autorelease
Summary:        Utilities for Google media downloads and resumable uploads

License:        Apache-2.0
URL:            https://github.com/googleapis/google-resumable-media-python
Source:         %{url}/archive/v%{version}/google-resumable-media-python-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist brotli}
%endif

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


%prep
%autosetup -n google-resumable-media-python-%{version}


%generate_buildrequires
%pyproject_buildrequires -x requests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l google


%check
%pyproject_check_import
%if %{with tests}
# Work around an usual pytest/PEP 420 issue where pytest can't import the
# installed module. Thanks to mhroncok for the help!
mv google{,_}
%pytest tests/unit
mv google{_,}
%endif


%files -n python3-google-resumable-media -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.rst


%changelog
%autochangelog
