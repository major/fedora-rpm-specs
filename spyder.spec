
%global _description %{expand:
Spyder is a powerful scientific environment written in Python, for Python, and 
designed by and for scientists, engineers and data analysts. It features a 
unique combination of the advanced editing, analysis, debugging and profiling 
functionality of a comprehensive development tool with the data exploration, 
interactive execution, deep inspection and beautiful visualization capabilities 
of an analysis package. Furthermore, Spyder offers built-in integration with 
many popular scientific libraries, including NumPy, SciPy, Pandas, IPython, 
QtConsole, Matplotlib, SymPy, and more, and can be extended further with 
full plugin support.
}

Name:		spyder
Version:	5.3.1
Release:	%autorelease
Summary:	Scientific Python Development Environment

Source0:	https://github.com/%{name}-ide/%{name}/archive/v%{version}.tar.gz

Patch0:		%{name}-%{version}_relax_versions.patch
License:	MIT
URL:		https://www.spyder-ide.org/
BuildArch:	noarch


%description
%_description

%package -n python3-%{name}
Summary:	%{summary}

%{?python_provide:%python_provide python3-%{name}}

BuildRequires:	python3-devel
BuildRequires:	python3-sphinx
BuildRequires:	python3-setuptools
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

Requires:	hicolor-icon-theme
Requires:	mathjax

%description -n python3-%{name}
%_description

%prep
%setup -q -n %{name}-%{version}
sed -i 's/\xe2\x80\x8b//g' scripts/org.spyder_ide.spyder.appdata.xml

%patch0

rm -rf PKG-INFO external-deps

# Remove DOS line endings
for file in `find -name "*.rst" -o -name "*.py" -o -name "*.css"`; do
	sed "s|\r||g" $file > $file.new && \
	touch -r $file $file.new && \
	mv $file.new $file
done

# remove bundled mathjax
rm -rvf spyder/plugins/help/utils/js/mathjax


%build
%py3_build


%install
mkdir -p %{buildroot}%{_datadir}/appdata
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%py3_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications scripts/%{name}.desktop

# install appdata file
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.spyder_ide.spyder.appdata.xml

# cleanup
rm -rvf %{buildroot}%{python3_sitelib}/spyderlib/doc/{.buildinfo,.doctrees}
rm -rvf %{buildroot}%{_bindir}/spyder_win_post_install.py

# replace bundled mathjax with a symlink to the system mathjax
ln -s %{_datadir}/javascript/mathjax/ \
    %{buildroot}%{python3_sitelib}/spyder/plugins/help/utils/js/mathjax

# provide spyder3 as symlink to spyder binary for continuity
ln -s %{_bindir}/spyder %{buildroot}%{_bindir}/spyder3

%ldconfig_scriptlets


%pretrans -n python3-%{name} -p <lua>
--[[Back up any bundled mathjax directory from the old package. See:
https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement
]]
path = "%{python3_sitelib}/spyder/plugins/help/utils/js/mathjax"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end


%files -n python3-%{name}
%{python3_sitelib}/spyder-*.egg-info
%{python3_sitelib}/spyder/
# A backed-up bundled mathjax directory from a previous upgrade may be present:
%ghost %{python3_sitelib}/spyder/plugins/help/utils/js/mathjax.rpmmoved
%{_bindir}/%{name}
%{_bindir}/%{name}3
%{_datadir}/metainfo/org.spyder_ide.spyder.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/spyder.png


%changelog
%autochangelog
