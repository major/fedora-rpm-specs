Name:           jedit
Version:        5.6.0
Release:        6%{?dist}
Summary:        Programmer's text editor

License:        GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later
URL:            http://www.jedit.org/
Source0:        https://sourceforge.net/projects/jedit/files/jedit/%{version}/jedit%{version}source.tar.bz2

BuildRequires:  ant apache-ivy ant-junit ivy-local junit bsf bsh ant-contrib ant-apache-bsf mockito hamcrest jsr-305 desktop-file-utils docbook-style-xsl xerces-j2 xalan-j2
Requires:       java >= 1:11
Requires:       javapackages-filesystem
Requires:       which

BuildArch: noarch
ExclusiveArch: %{java_arches} noarch

%description
jEdit is an Open Source, cross platform text editor written in Java. It
has an extensive feature set that includes syntax highlighting, auto indent,
folding, word wrap, abbreviation expansion, multiple clipboards, powerful search
and replace, and much more.

Futhermore, jEdit is extremely customizable, and extensible, using either macros
written in the BeanShell scripting language, or plugins written in Java.

%prep
%setup -q -n jEdit

# remove unnecessary dependencies (not required for default build)
sed -i '/<dependency org="net.sf.docbook" name="docbook-xsl"/,/<\/dependency>/d' ivy.xml
sed -i '/<dependency org="net.sf.docbook" name="docbook-xsl-saxon"/d' ivy.xml
sed -i '/<dependency org="org.apache.xmlgraphics" name="fop"/d' ivy.xml
sed -i '/<dependency org="net.sf.launch4j" name="launch4j"/,/<\/dependency>/d' ivy.xml
sed -i '/<dependency org="org.bouncycastle"/d' ivy.xml
sed -i '/<dependency org="com.evolvedbinary.appbundler"/d' ivy.xml

# fix mockito dependency
sed -i 's;name="mockito-junit-jupiter";name="mockito-core";g' ivy.xml

# skip downloading of binary plugins
sed -i '/<dependency org="org.jedit.plugins"/d' ivy.xml
sed -i '/<script language="javascript">/,/<[/]script>/d' build.xml
sed -i 's;<ivy:retrieve.*/>;&\n<mkdir dir="${lib.dir}/default-plugins"/>;g' build.xml

# fix docs generation
# docbook-xsl not available as xmvn artifact in fedora, supply zip manually
ln -s /usr/share/sgml/docbook/xsl-stylesheets docbook
zip -rq docbook-xsl-resources.zip docbook
sed -i 's;${lib.dir}/docbook/docbook-xsl-resources.zip;docbook-xsl-resources.zip;g' build.xml
# saxon not available in fedora, use xalan instead
sed -i 's;<dependency org="saxon" name="saxon" rev="[0-9.]*" conf="docbook"/>;<dependency org="xalan" name="xalan" rev="2.7.2" conf="docbook"/><dependency org="xalan" name="serializer" rev="2.7.2" conf="docbook"/>;g' ivy.xml
sed -i 's;com.icl.saxon.TransformerFactoryImpl;org.apache.xalan.processor.TransformerFactoryImpl;g' build.xml

# use system ivy configuration
rm -f ivysettings.xml
sed -i '/<ivy:settings.*[/]>/d' build.xml

%build
ant -Divy.mode=local -Divy.jar.present=true build docs-html

%install
mkdir -p %{buildroot}%{_javadir}
cp -pR build/%{name}.jar %{buildroot}%{_javadir}/

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pR build/{doc,jars,keymaps,macros,modes,properties,startup} %{buildroot}%{_datadir}/%{name}
ln -s ../java/%{name}.jar %{buildroot}%{_datadir}/%{name}/%{name}.jar

mkdir -p %{buildroot}%{_bindir}
cp -p package-files/linux/jedit %{buildroot}%{_bindir}/jedit
sed -i 's;/usr/share/jEdit/@jar.filename@;%{_datadir}/%{name}/%{name}.jar;g' %{buildroot}%{_bindir}/jedit
chmod +x %{buildroot}%{_bindir}/jedit

mkdir -p %{buildroot}%{_mandir}/man1
cp -p package-files/linux/jedit.1 %{buildroot}%{_mandir}/man1/jedit.1
sed -i 's;@jedit.version@;%{version};g' %{buildroot}%{_mandir}/man1/jedit.1

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications --set-icon=%{_datadir}/%{name}/doc/%{name}.png package-files/linux/deb/%{name}.desktop

%files
%{_javadir}/%{name}.jar
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/jedit.1*
%{_datadir}/applications/jedit.desktop
%doc doc/README.txt
%license doc/COPYING.txt
%license doc/COPYING.DOC.txt
%license doc/COPYING.PLUGINS.txt
%license doc/Apache.LICENSE.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 11 2024 Zdenek Zambersky <zzambers@redhat.com> - 5.6.0-5
- Added xalan serializer dependency to fix build problem on f41

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 Zdenek Zambersky <zzambers@redhat.com> - 5.6.0-1
- Initial package
