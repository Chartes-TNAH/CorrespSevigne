<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" encoding="UTF-8"/>
    
    <xsl:param name="numero"/>
    <xsl:param name="ref"/>
    
    <xsl:template match="/" >
        <div class="container">
            <div class="col-md-6 offset-md-3">
                <xsl:apply-templates select="//text[@n=$ref]"/>
            </div>
        </div>
    </xsl:template>

    <xsl:template match="text">
        <xsl:apply-templates/>
    </xsl:template>
    <!--
    <xsl:template match="text">
        <xsl:if test="./@ref=$ref">
            <xsl:apply-templates/>
        </xsl:if>
    </xsl:template>
    -->

    <xsl:template match="body">
        <xsl:apply-templates select="./div1"/>
    </xsl:template>
    
    <xsl:template match="div1">
        <div>
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    
    <xsl:template match="head">
        <h5>
            <p class="correspondants">
                <xsl:value-of select="p[1]"/>
            </p>
            <p class="font-italic">
                <xsl:value-of select="p[2]"/>
            </p>
        </h5>
    </xsl:template>
    
    <xsl:template match="lb">
        <xsl:element name="br"/>
    </xsl:template>
    
    <xsl:template match="div2">
        <span>
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    
    <xsl:template match="p">
        <p class="corps">
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <xsl:template match="div3">
        <p class="ajout">
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
</xsl:stylesheet>
