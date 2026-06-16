Name:           python-scales
Version:        1.0.9
Release:        %autorelease
Summary:        Stats for Python processes

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/Cue/scales
Source0:        %{url}/archive/%{version}.tar.gz

# https://github.com/Cue/scales/pull/47
Patch0:         fix_py38_compatibility.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildRequires:  python3-simplejson
BuildRequires:  python3-pytest
BuildRequires:  python3-pkg-resources

%global _description\
Tracks server state and statistics, allowing you to see what your server is\
doing. It can also send metrics to Graphite for graphing or to a file for crash\
forensics.\


%description %_description

%package -n python3-scales
Summary:        Stats for Python 3 processes
Requires:       python3-six
Requires:       python3-simplejson

%description -n python3-scales %_description


%prep
%setup -q -n scales-%{version}
%patch -P0 -p1
# Python 3.11 compatibility
sed -i "s/self.assertEquals/self.assertEqual/g" \
    src/greplin/scales/scales_test.py \
    src/greplin/scales/aggregation_test.py \
    src/greplin/scales/formats_test.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l greplin

%check
%pytest


%files -n python3-scales -f %{pyproject_files}
%{python3_sitelib}/scales*.pth
%doc AUTHORS LICENSE README.md


%changelog
%autochangelog
