# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/qtree
# catalog-date 2009-01-24 16:10:54 +0100
# catalog-license lppl
# catalog-version 3.1b
Name:		texlive-qtree
Version:	3.1b
Release:	1
Summary:	Draw tree structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qtree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qtree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qtree.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package offers support for drawing tree diagrams, and is
especially suitable for linguistics use. It allows trees to be
specified in a simple bracket notation, automatically
calculates branch sizes, and supports both DVI/PostScript and
PDF output by use of pict2e facilities. The package is a
development of the existing qobitree package, offering a new
front end.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/qtree/qtree.sty
%doc %{_texmfdistdir}/doc/latex/qtree/README
%doc %{_texmfdistdir}/doc/latex/qtree/qarrows.pdf
%doc %{_texmfdistdir}/doc/latex/qtree/qarrows.tex
%doc %{_texmfdistdir}/doc/latex/qtree/qtreenotes.pdf
%doc %{_texmfdistdir}/doc/latex/qtree/qtreenotes.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
