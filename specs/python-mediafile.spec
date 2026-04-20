%global shortname mediafile
Name:           python-mediafile
Version:        0.16.2
Release:        %autorelease
Summary:        Elegant audio file tagging in Python

License:        MIT
URL:            http://pypi.org/project/mediafile/
Source0:        %{pypi_source mediafile}

BuildArch:     noarch
BuildRequires:  python3-devel

%global _description %{expand:
MediaFile is a simple interface to the metadata tags for many audio file
formats. It wraps Mutagen, a high-quality library for low-level tag
manipulation, with a high-level, format-independent interface for a common set
of tags.}

%description %{_description}

%package -n python3-%{shortname}
Summary:        %{summary}

Requires:       python3 >= 3.10
Requires:       python3-filetype >= 1.2.0
Requires:       python3-mutagen

%description -n python3-%{shortname} %{_description}

Python 3 version.

%prep
%autosetup -n %{shortname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check

%install
%pyproject_install
%pyproject_save_files '*%{shortname}*'

%files -n python3-%{shortname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%autochangelog
