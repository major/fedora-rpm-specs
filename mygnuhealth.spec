Name:           mygnuhealth
Version:        1.0.5
Release:        %autorelease
Summary:        The GNU Health Personal Health Record (PHR)

License:        GPLv3+
URL:            https://www.gnuhealth.org 
Source:         https://ftp.gnu.org/gnu/health/mygnuhealth/mygnuhealth-%{version}.tar.gz
# https://lists.gnu.org/archive/html/health/2022-01/msg00008.html
Patch0:         metainfo.patch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       kf5-kirigami2
Requires:       python3-pyside2

Provides:       python3-mygnuhealth

BuildArch:      noarch

%description
MyGNUHealth is a desktop and mobile application that helps you to take
control of your health. As a Personal Health Record, you will be able
to record, assess and proactively take action upon the determinants of
the main health spheres (bio-psycho-social).
MyGNUHealth will be your health companion. You will be able to connect
with your health professionals, and share the health data you wish to
share with them in real time.
MyGNUHealth puts you in the driver's seat, as an active member of the
system of health.

%package doc
Summary:        Additional documentation files for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mygnuhealth

# Proposed upstream to change the name
# https://lists.gnu.org/archive/html/health/2022-01/msg00008.html
mv %{buildroot}%{_datadir}/applications/org.kde.mygnuhealth.desktop \
   %{buildroot}%{_datadir}/applications/org.gnuhealth.mygnuhealth.desktop
mv %{buildroot}%{_metainfodir}/org.kde.mygnuhealth.metainfo.xml \
   %{buildroot}%{_metainfodir}/org.gnuhealth.mygnuhealth.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnuhealth.mygnuhealth.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnuhealth.mygnuhealth.metainfo.xml

%files -f %{pyproject_files}
%license LICENSE COPYRIGHT
%doc Changelog README.rst
%{_bindir}/mygnuhealth
%{_datadir}/applications/org.gnuhealth.mygnuhealth.desktop
%{_datadir}/icons/hicolor/scalable/apps/mygnuhealth.svg
%{_metainfodir}/org.gnuhealth.mygnuhealth.metainfo.xml

%files doc
%doc %{_docdir}/mygnuhealth

%changelog
%autochangelog
