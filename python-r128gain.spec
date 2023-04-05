%global modname r128gain
%global projname %{modname}

# The tests require network access, so disable them by default
%bcond_with tests

Name:           python-%{projname}
Version:        1.0.7
Release:        %autorelease
Summary:        Fast audio loudness scanner & tagger

License:        LGPL-2.1-or-later
URL:            https://github.com/desbma/%{projname}
Source0:        %{url}/archive/%{version}/%{projname}-%{version}.tar.gz

# Needed to allow the use of argparse-manpage to generate a manpage
Patch:          0000-expose-arg-parser.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  argparse-manpage

%if %{with tests}
BuildRequires:  python3-requests
BuildRequires:  sox
%endif

%global _description %{expand:
r128gain is a multi platform command line tool to scan your audio files and
tag them with loudness metadata (ReplayGain v2 or Opus R128 gain format), to
allow playback of several tracks or albums at a similar loudness level.
r128gain can also be used as a Python module from other Python projects to
scan and/or tag audio files.}

%description %_description

%package     -n python3-%{projname}
Summary:        %{summary}

%description -n python3-%{projname} %_description

%prep
%autosetup -n %{projname}-%{version} -p1

# Remove unwanted shebangs
sed -i /^#!/d r128gain/{__init__,__main__}.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Generate a basic manpage
PYTHONPATH=. argparse-manpage \
    --prog %{modname} --module %{modname} \
    --function get_arg_parser --author desbma \
    --project-name %{name} --url %{url} \
    >%{modname}.1

%install
%pyproject_install
%pyproject_save_files %{modname}

install -d %{buildroot}%{_mandir}/man1
install -pm 0644 %{modname}.1 %{buildroot}%{_mandir}/man1

%check
%if %{with tests}
%python3 setup.py test
%else
%pyproject_check_import
%endif

%files -n python3-%{projname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{modname}
%{_mandir}/man1/%{modname}.1*

%changelog
%autochangelog
