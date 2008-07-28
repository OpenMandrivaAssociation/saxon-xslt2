Summary:	Saxon XSLT2 Processor in Java
Name: 		saxon-xslt2
Version: 	7.8
Release: 	%mkrel 3
License: 	MPL
Group: 		Publishing
Url:		http://saxon.sourceforge.net/
Source: 	http://prdownloads.sourceforge.net/saxon/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot 
BuildArch:	noarch

Requires:	jre

%define	_javaclassdir	%{_datadir}/java/classes/%{name}

%description
The SAXON package is a collection of tools for processing XML
documents, compliant with the XSLT2 recommendation.

%prep
%setup -q

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

chmod a-x *.jar
install -d $RPM_BUILD_ROOT%{_javaclassdir}
install saxon7*.jar $RPM_BUILD_ROOT%{_javaclassdir}

mkdir -p $RPM_BUILD_ROOT/%{_prefix}/bin
cat << EOF > $RPM_BUILD_ROOT/%{_prefix}/bin/saxon7batch
#!/bin/bash

export CLASSPATH=$CLASSPATH:%{_javaclassdir}/saxon7.jar
java net.sf.saxon.Transform \$*
EOF
chmod 555 $RPM_BUILD_ROOT/%{_prefix}/bin/saxon7batch


%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc samples use-cases
%dir %{_datadir}/java/classes/
%dir %{_javaclassdir}/
#%{_javaclassdir}
%{_javaclassdir}/*
%attr(755,root,root) %{_prefix}/bin/saxon7batch


