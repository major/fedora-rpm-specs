%global srcname paperwork

Name:           %{srcname}
Version:        2.1.1
Release:        %autorelease
Summary:        Using scanner and OCR to grep dead trees the easy way

License:        GPLv3+
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork
Source0:        %{pypi_source}
Patch0001:      0001-Drop-extra-icon-dirs.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel

Requires:       hicolor-icon-theme
Requires:       python3-%{srcname} = %{version}-%{release}

%global _description %{expand: \
Paperwork is a tool to make papers searchable.

The basic idea behind Paperwork is "scan & forget": You should be able to just
scan a new document and forget about it until the day you need it again.

Let the machine do most of the work.
}

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-gobject
BuildRequires:  libnotify
BuildRequires:  /usr/bin/xvfb-run

# Fallback to old orientation heuristic just freezes, so ensure this is
# available.
Requires:       tesseract-osd
Requires:       libinsane-gobject

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version} -p2

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    xvfb-run -a \
        python3 -m paperwork_gtk.main install \
            --data_base_dir %{buildroot}%{_datadir} \
            --icon_base_dir %{buildroot}%{_datadir}/icons

%pyproject_save_files paperwork_gtk

%check
export PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=%{buildroot}%{python3_sitelib}

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

xvfb-run -a paperwork-gtk chkdeps
xvfb-run -a %{python3} -m unittest discover --verbose -s tests

%files
%{_bindir}/paperwork-gtk
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.markdown

%changelog
%autochangelog
